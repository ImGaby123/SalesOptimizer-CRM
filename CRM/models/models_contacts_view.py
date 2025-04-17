from PySide6.QtWidgets import QWidget, QMessageBox
from views.py.ui_contacts_view import Ui_contacts_view
from datas.db_connection import DB_Connection

class ContactsView(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.ui = Ui_contacts_view()
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()
        self.contact_id = contact_id

        self.connect_signals()
        self.load_contact_details()

    def connect_signals(self):
        """Connects UI signals to their handlers."""
        self.ui.back_line.clicked.connect(self.go_back)

    def go_back(self):
        """Navigates back to the ContactsLanding form."""
        from models.models_authentication import MDIManager
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        """Fetches and displays contact, company, and address info."""
        query = """
            SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender, c.job_title,
                   ca.street AS contact_street, ca.city AS contact_city, ca.state AS contact_state,
                   ca.zip_code AS contact_zip_code, ca.country AS contact_country,
                   ca_comp.street AS company_street, ca_comp.city AS company_city, ca_comp.state AS company_state,
                   ca_comp.zip_code AS company_zip_code, ca_comp.country AS company_country,
                   COALESCE(comp.company_name, '') AS company_name,
                   comp.company_email, comp.website, comp.industry,
                   ls.source_name, ca_comp.address_type
            FROM contact c
            LEFT JOIN contact_address ca ON c.contact_id = ca.contact_id
            LEFT JOIN company comp ON c.company_id = comp.company_id
            LEFT JOIN company_address ca_comp ON comp.company_id = ca_comp.company_id
            LEFT JOIN leads l ON c.contact_id = l.contact_id
            LEFT JOIN lead_source ls ON l.source_id = ls.source_id
            WHERE c.contact_id = %s
        """
        contact = self.db_conn.fetch_one(query, (self.contact_id,))
        if not contact:
            QMessageBox.warning(self, "Error", "Contact not found.")
            return

        # Contact info
        self.ui.firstname_line.setText(contact.get("first_name", ""))
        self.ui.lastname_line.setText(contact.get("last_name", ""))
        self.ui.email_line.setText(contact.get("email", ""))
        self.ui.phone_line.setText(contact.get("phone_number", ""))
        self.ui.gender_combo.setCurrentText(contact.get("gender", ""))
        self.ui.title_combo.setCurrentText(contact.get("job_title", ""))

        # Company info
        self.ui.company_line.setText(contact.get("company_name", ""))
        self.ui.company_email_line.setText(contact.get("company_email", ""))
        self.ui.company_website_line.setText(contact.get("website", ""))
        self.ui.company_industry_combo.setCurrentText(contact.get("industry", ""))

        # Lead source
        self.ui.source_name_line.setText(contact.get("source_name", ""))

        # Contact address
        self.ui.street_line.setText(contact.get("contact_street", ""))
        self.ui.city_combo.setCurrentText(contact.get("contact_city", ""))
        self.ui.state_line.setText(contact.get("contact_state", ""))
        self.ui.zip_line.setText(contact.get("contact_zip_code", ""))
        self.ui.country_combo.setCurrentText(contact.get("contact_country", ""))

        # Company address
        self.ui.company_street_line.setText(contact.get("company_street", ""))
        self.ui.company_city_combo.setCurrentText(contact.get("company_city", ""))
        self.ui.company_state_line.setText(contact.get("company_state", ""))
        self.ui.company_zip_line.setText(contact.get("company_zip_code", ""))
        self.ui.company_country_combo.setCurrentText(contact.get("company_country", ""))

        # Address type
        address_type = contact.get("address_type", "")
        if address_type in ["Billing", "Shipping", "Office"]:
            self.ui.address_type_combo.setCurrentText(address_type)
        else:
            self.ui.address_type_combo.setCurrentIndex(0)
