from PySide6.QtWidgets import QDialog, QMessageBox, QSizePolicy
from PySide6.QtCore import QDate
from views.py.ui_add_campaign import Ui_add_campaign
from datas.db_connection import DB_Connection

class AddCampaign(QDialog):
    def __init__(self, contact_id=None, opportunity_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_campaign()
        self.contact_id = contact_id
        self.opportunity_id = opportunity_id
        self.db = DB_Connection()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Initialize UI
        self.ui.date_edit.setDate(QDate.currentDate())
        self.load_opportunity_title()

        # Connect buttons
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.save_btn.clicked.connect(self.add_campaign)

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

    def add_campaign(self):
        """Insert a new campaign record into campaign_timeline."""
        action = self.ui.action_line.text().strip()
        campaign_type = self.ui.campaign_type_combo.currentText().strip()
        campaign_details = self.ui.details_text.toPlainText().strip()
        campaign_date = self.ui.date_edit.text()

        if not all([action, campaign_type, campaign_details]):
            QMessageBox.warning(self, "Missing Fields", "Please fill in all fields before saving.")
            return

        insert_query = """
            INSERT INTO campaign_timeline (opportunity_id, campaign_details, action, type, campaign_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        success = self.db.execute_query(insert_query, (
            self.opportunity_id,
            campaign_details,
            action,
            campaign_type,
            campaign_date
        ))

        if success:
            QMessageBox.information(self, "Success", "📢 Campaign added successfully.")
            self.accept()

            # Reload LeadsProfile view
            from models.models_authentication import MDIManager
            from models.models_leads_profile import LeadsProfile
            MDIManager.load_into_mdi(lambda: LeadsProfile(self.contact_id))
        else:
            QMessageBox.critical(self, "Error", "❌ Failed to add campaign.")
