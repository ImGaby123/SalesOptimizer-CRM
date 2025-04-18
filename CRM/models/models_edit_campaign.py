from PySide6.QtWidgets import QDialog, QMessageBox, QSizePolicy
from PySide6.QtCore import Qt, QDate
from datetime import datetime
from views.py.ui_edit_campaign import Ui_edit_campaign
from datas.db_connection import DB_Connection

class EditCampaign(QDialog):
    def __init__(self, contact_id=None, opportunity_id=None, campaign_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_edit_campaign()
        self.contact_id = contact_id
        self.opportunity_id = opportunity_id
        self.campaign_id = campaign_id
        self.db = DB_Connection()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Initialize UI
        self.load_opportunity_title()
        self.load_campaign_details()

        # Connect buttons
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.edit_campaign)

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

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_position)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()
    def load_opportunity_title(self):
        """Fetch and display the opportunity title based on opportunity_id."""
        query = """
            SELECT opportunity_title
            FROM opportunity
            WHERE opportunity_id = %s AND contact_id = %s
        """
        result = self.db.fetch_one(query, (self.opportunity_id, self.contact_id))
        if result:
            self.ui.opportunity_title_line.setText(result["opportunity_title"])
        else:
            QMessageBox.warning(self, "Not Found", "Opportunity title could not be loaded.")

    def load_campaign_details(self):
        """Pre-fill the form with existing campaign details."""
        query = """
            SELECT action, type, campaign_details, campaign_date
            FROM campaign_timeline
            WHERE campaign_id = %s AND opportunity_id = %s
        """
        result = self.db.fetch_one(query, (self.campaign_id, self.opportunity_id))
        if result:
            self.ui.action_line.setText(result["action"])
            self.ui.campaign_type_combo.setCurrentText(result["type"])
            self.ui.details_text.setPlainText(result["campaign_details"])

            # Ensure the campaign_date is in 'yyyy-MM-dd' format
            campaign_date = result["campaign_date"]

            # Convert the date to a string if it's a datetime object
            if isinstance(campaign_date, datetime):
                campaign_date_str = campaign_date.strftime("%Y-%m-%d")
            else:
                campaign_date_str = str(campaign_date)  # Assuming it's already in a proper string format

            try:
                # Parse the date string ('yyyy-MM-dd') into a QDate object
                campaign_date_obj = QDate.fromString(campaign_date_str, "yyyy-MM-dd")
                if campaign_date_obj.isValid():
                    self.ui.date_edit.setDate(campaign_date_obj)
                else:
                    QMessageBox.warning(self, "Invalid Date", "The campaign date could not be parsed correctly.")
            except Exception as e:
                QMessageBox.warning(self, "Parsing Error", f"An error occurred while parsing the date: {str(e)}")
        else:
            QMessageBox.warning(self, "Not Found", "Campaign details could not be loaded.")

    def edit_campaign(self):
        """Update the campaign record."""
        action = self.ui.action_line.text().strip()
        campaign_type = self.ui.campaign_type_combo.currentText().strip()
        campaign_details = self.ui.details_text.toPlainText().strip()
        campaign_date = self.ui.date_edit.text()

        if not all([action, campaign_type, campaign_details]):
            QMessageBox.warning(self, "Missing Fields", "Please fill in all fields before saving.")
            return

        update_query = """
            UPDATE campaign_timeline
            SET action = %s, type = %s, campaign_details = %s, campaign_date = %s
            WHERE campaign_id = %s
        """
        success = self.db.execute_query(update_query, (
            action,
            campaign_type,
            campaign_details,
            campaign_date,
            self.campaign_id
        ))

        if success:
            QMessageBox.information(self, "Success", "✅ Campaign updated successfully.")
            self.accept()

            # Reload LeadsProfile view
            from models.models_authentication import MDIManager
            from models.models_leads_profile import LeadsProfile
            MDIManager.load_into_mdi(lambda: LeadsProfile(self.contact_id))
        else:
            QMessageBox.critical(self, "Error", "❌ Failed to update campaign.")
