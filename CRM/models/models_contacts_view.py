from PySide6.QtWidgets import QWidget, QMessageBox
from views.py.ui_contacts_view import Ui_contacts_view  # Assuming the Ui file is auto-generated
from datas.db_connection import DB_Connection

class ContactsView(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.ui = Ui_contacts_view()  # UI setup
        self.ui.setupUi(self)

        # Initialize DB connection
        self.db_conn = DB_Connection()
        self.contact_id = contact_id

        # Connect the back button to go back to the landing page
        self.ui.back_line.clicked.connect(self.go_back)

        # Load contact details when the form is initialized
        self.load_contact_details()

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        """Fetches and displays contact details, including company and contact address."""
        query = """
        SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender, c.job_title,
               ca.street AS contact_street, ca.city AS contact_city, ca.state AS contact_state,
               ca.zip_code AS contact_zip_code, ca.country AS contact_country,
               ca_comp.street AS company_street, ca_comp.city AS company_city, ca_comp.state AS company_state,
               ca_comp.zip_code AS company_zip_code, ca_comp.country AS company_country,
               COALESCE(comp.company_name, '') AS company_name,
               comp.company_email, comp.website, comp.industry,
               ls.source_name, ca_comp.address_type  -- Added address_type here
        FROM contact c
        LEFT JOIN contact_address ca ON c.contact_id = ca.contact_id  -- contact address
        LEFT JOIN company comp ON c.company_id = comp.company_id
        LEFT JOIN company_address ca_comp ON comp.company_id = ca_comp.company_id  -- company address
        LEFT JOIN leads l ON c.contact_id = l.contact_id
        LEFT JOIN lead_source ls ON l.source_id = ls.source_id
        WHERE c.contact_id = %s
        """

        contact = self.db_conn.fetch_one(query, (self.contact_id,))
        if contact:
            # Set the contact details into the corresponding UI fields
            self.ui.firstname_line.setText(contact.get("first_name", ""))
            self.ui.lastname_line.setText(contact.get("last_name", ""))
            self.ui.email_line.setText(contact.get("email", ""))
            self.ui.phone_line.setText(contact.get("phone_number", ""))
            self.ui.gender_combo.setCurrentText(contact.get("gender", ""))
            self.ui.title_line.setText(contact.get("job_title", ""))

            # Set company information
            self.ui.company_line.setText(contact.get("company_name", ""))
            self.ui.company_email_line.setText(contact.get("company_email", ""))
            self.ui.company_website_line.setText(contact.get("website", ""))
            self.ui.company_industry_line.setText(contact.get("industry", ""))

            # Set lead source information
            self.ui.source_name_line.setText(contact.get("source_name", ""))

            # Set contact's address information
            self.ui.street_line.setText(contact.get("contact_street", ""))
            self.ui.city_line.setText(contact.get("contact_city", ""))
            self.ui.state_line.setText(contact.get("contact_state", ""))
            self.ui.zip_line.setText(contact.get("contact_zip_code", ""))
            self.ui.country_line.setText(contact.get("contact_country", ""))

            # Set company address information
            self.ui.company_street_line.setText(contact.get("company_street", ""))
            self.ui.company_city_line.setText(contact.get("company_city", ""))
            self.ui.company_state_line.setText(contact.get("company_state", ""))
            self.ui.company_zip_line.setText(contact.get("company_zip_code", ""))
            self.ui.company_country_line.setText(contact.get("company_country", ""))

            # Set the address_type in the address_type_combo (combo box)
            address_type = contact.get("address_type", "")
            if address_type in ["Billing", "Shipping", "Office"]:
                self.ui.address_type_combo.setCurrentText(address_type)
            else:
                self.ui.address_type_combo.setCurrentIndex(0)  # Default to the first option if it doesn't match

        else:
            QMessageBox.warning(self, "Error", "Contact not found.")
