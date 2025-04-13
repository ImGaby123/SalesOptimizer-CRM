from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate, Signal
from views.py.ui_edit_opportunity import Ui_edit_opportunity
from datas.db_connection import DB_Connection
from models.models_authentication import MDIManager
from models.models_leads_profile import LeadsProfile


class EditOpportunity(QDialog):
    updated = Signal()  # Signals to refresh opportunities table in the LeadsProfile

    def __init__(self, contact_id=None, opportunity_id=None, parent=None):
        super().__init__(parent)
        self.contact_id = contact_id
        self.opportunity_id = opportunity_id
        self.ui = Ui_edit_opportunity()
        self.ui.setupUi(self)

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Rounded corners style
        self.ui.main_frame.setStyleSheet("""
            background-color: #171717;
            border-radius: 10px;
        """)

        self.db = DB_Connection()

        # Make window draggable
        self.drag_position = None
        self.ui.date_edit.setDate(QDate.currentDate())  # Set current date

        # Populate opportunity data
        self.load_opportunity_data()

        # Connect buttons to their handlers
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.save_opportunity)

    def mousePressEvent(self, event):
        """Enable window dragging."""
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        """Move the window while dragging."""
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_position)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def load_opportunity_data(self):
        """Load data of the selected opportunity into the dialog."""
        query = """
            SELECT opportunity_title, opportunity_cost, opportunity_details, date
            FROM opportunity
            WHERE opportunity_id = %s
        """
        data = self.db.fetch_one(query, (self.opportunity_id,))

        if data:
            self.ui.title_line.setText(data["opportunity_title"] or "")
            self.ui.cost_line.setText(str(data["opportunity_cost"]) if data["opportunity_cost"] else "")
            self.ui.details_text.setPlainText(data["opportunity_details"] or "")
            if data["date"]:
                d = data["date"]
                self.ui.date_edit.setDate(QDate(d.year, d.month, d.day))

    def save_opportunity(self):
        """Validate and save opportunity data."""
        title = self.ui.title_line.text().strip()
        cost_text = self.ui.cost_line.text().replace(",", "").replace("$", "")
        details = self.ui.details_text.toPlainText().strip()
        date = self.ui.date_edit.text()

        if not title:
            QMessageBox.warning(self, "Validation Error", "Opportunity title is required.")
            return

        try:
            cost = float(cost_text) if cost_text else None
        except ValueError:
            QMessageBox.warning(self, "Validation Error", "Invalid opportunity cost.")
            return

        confirm = QMessageBox.question(
            self, "Confirm", "Are you sure you want to save changes?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            return

        update_query = """
            UPDATE opportunity
            SET opportunity_title = %s,
                opportunity_cost = %s,
                opportunity_details = %s,
                date = %s
            WHERE opportunity_id = %s
        """
        values = (title, cost, details, date, self.opportunity_id)

        try:
            self.db.execute_query(update_query, values)
            QMessageBox.information(self, "Success", "Opportunity updated successfully.")

            # Trigger MDIManager to refresh the LeadsProfile
            if self.parent() and hasattr(self.parent(), "contact_id"):
                MDIManager.load_into_mdi(lambda: LeadsProfile(self.parent().contact_id))

            self.accept()  # Close the dialog after success
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update opportunity:\n{e}")
