from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate
from views.py.ui_add_opportunity import Ui_add_opportunity
from datas.db_connection import DB_Connection

class AddOpportunity(QDialog):
    def __init__(self, contact_id=None, parent=None):
        super().__init__(parent)
        self.contact_id = contact_id
        self.ui = Ui_add_opportunity()
        self.ui.setupUi(self)

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Rounded corners
        self.ui.main_frame.setStyleSheet("""
            background-color: #171717;
            border-radius: 10px;
        """)

        # Make window draggable
        self.drag_position = None

        # Get Current Date
        self.ui.date_edit.setDate(QDate.currentDate())

        # Cancel button closes window
        self.ui.cancel_btn.clicked.connect(self.close)

        # Add button triggers opportunity insert
        self.ui.add_btn.clicked.connect(self.add_opportunity)

        # Database connection
        self.db = DB_Connection()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_position)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def add_opportunity(self):
        # Get values from the form
        title = self.ui.title_line.text().strip()
        cost_text = self.ui.cost_line.text()
        cost_text = cost_text.replace(",", "").replace("$", "")
        details = self.ui.details_text.toPlainText().strip()
        date = self.ui.date_edit.text()  # Assumes format YYYY/MM/DD

        # Validate required field
        if not title:
            QMessageBox.warning(self, "Validation Error", "Opportunity title is required.")
            return

        # Optional: Convert cost to decimal
        try:
            cost = float(cost_text) if cost_text else None
        except ValueError:
            QMessageBox.warning(self, "Validation Error", "Invalid opportunity cost.")
            return

        # Confirm insertion
        confirm = QMessageBox.question(
            self, "Confirm", "Are you sure you want to add this opportunity?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        # Fetch lead_id and company_id
        lead_query = "SELECT lead_id, company_id FROM leads WHERE contact_id = %s"
        lead_data = self.db.fetch_one(lead_query, (self.contact_id,))
        if not lead_data:
            QMessageBox.critical(self, "Error", "Unable to find matching lead for this contact.")
            return

        lead_id = lead_data["lead_id"]
        company_id = lead_data["company_id"]

        # Insert query
        insert_query = """
            INSERT INTO opportunity (
                company_id, contact_id, lead_id,
                opportunity_title, opportunity_cost,
                opportunity_details, date
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            company_id,
            self.contact_id,
            lead_id,
            title,
            cost,
            details,
            date
        )

        # Execute insert
        try:
            self.db.execute_query(insert_query, values)
            QMessageBox.information(self, "Success", "Opportunity added successfully.")
            self.accept()  # Close dialog

            # Reload the LeadsProfile after successful addition
            from models.models_authentication import MDIManager
            from models.models_leads_profile import LeadsProfile
            MDIManager.load_into_mdi(lambda: LeadsProfile(self.contact_id))  # Reload LeadsProfile to show new opportunity

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add opportunity:\n{e}")
