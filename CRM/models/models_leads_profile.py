from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt
from views.py.ui_leads_profile import Ui_leads_profile
from datas.db_connection import DB_Connection

class LeadsProfile(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.contact_id = contact_id
        self.ui = Ui_leads_profile()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()

        # Load contact info and lead total & status
        self.contact_info()
        # self.lead_status_indicator()

        # View Full Contact Info
        self.ui.full_info_lbl.mousePressEvent = lambda event: self.view_contact_info()

        # Code for going back to leads_landing
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_leads_landing import LeadsLanding
        MDIManager.load_into_mdi(LeadsLanding)

    def view_contact_info(self):
        from models.models_authentication import MDIManager
        from models.models_contacts_view import ContactsView  # Adjust this import as needed

        contact_id = self.contact_id
        if not contact_id:
            return

        MDIManager.load_into_mdi(lambda: ContactsView(contact_id))

    def contact_info(self):
        """Loads contact information into the respective labels."""
        query = """
            SELECT c.first_name, c.last_name, c.phone_number, c.job_title, c.email,
                   comp.company_name, ls.source_name
            FROM contact c
            JOIN company comp ON c.company_id = comp.company_id
            LEFT JOIN lead_source ls ON c.contact_id = ls.source_id
            WHERE c.contact_id = %s
        """
        contact_data = self.db_conn.fetch_one(query, (self.contact_id,))

        if contact_data:
            name = f"{contact_data['first_name']} {contact_data['last_name']}"
            self.ui.name_lbl.setText(name)
            self.ui.name_lbl_2.setText(name)
            self.ui.email_lbl.setText(contact_data['email'])
            self.ui.company_lbl.setText(contact_data['company_name'])
            self.ui.company_lbl_2.setText(contact_data['company_name'])
            self.ui.lead_source_value_lbl.setText(contact_data['source_name'] if contact_data['source_name'] else "N/A")

    # def lead_status_indicator(self):
    #     """Updates the progress bar and radio buttons based on the lead status."""
    #     query = """
    #         SELECT l.lead_status
    #         FROM leads l
    #         WHERE l.contact_id = %s
    #     """
    #     lead_data = self.db_conn.fetch_one(query, (self.contact_id,))

    #     if lead_data:
    #         lead_status = lead_data['lead_status']

    #         # Set progress bar value based on lead_status
    #         progress_mapping = {
    #             'Lead': 5,
    #             'Prospecting': 22,
    #             'Qualifications': 39,
    #             'Contacting': 53,
    #             'Negotiating': 68,
    #             'Closed Lost': 83,
    #             'Closed Won': 100
    #         }

    #         progress_value = progress_mapping.get(lead_status, 0)
    #         self.ui.lead_status_bar.setValue(progress_value)  # Correct progress bar name

    #         # Set the radio buttons based on the lead status
    #         # Reset all radio buttons first
    #         self.ui.lead_radio.setChecked(False)
    #         self.ui.prospecting_radio.setChecked(False)
    #         self.ui.qualifications_radio.setChecked(False)
    #         self.ui.contacting_radio.setChecked(False)
    #         self.ui.negotiating_radio.setChecked(False)
    #         self.ui.loss_radio.setChecked(False)
    #         self.ui.won_radio.setChecked(False)

    #         # Set the radio buttons according to the lead's status
    #         if lead_status == 'Lead':
    #             self.ui.lead_radio.setChecked(True)
    #         if lead_status == 'Prospecting':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #         if lead_status == 'Qualifications':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #         if lead_status == 'Contacting':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #         if lead_status == 'Negotiating':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #         if lead_status == 'Closed Lost':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #             self.ui.loss_radio.setChecked(True)
    #         if lead_status == 'Closed Won':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #             self.ui.loss_radio.setChecked(True)
    #             self.ui.won_radio.setChecked(True)

