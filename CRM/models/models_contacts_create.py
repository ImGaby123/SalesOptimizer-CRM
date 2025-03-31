from PySide6.QtWidgets import QWidget, QMessageBox
from views.py.ui_contacts_create import Ui_contacts_create
from datas.db_connection import DB_Connection

class ContactsCreate(QWidget):
    def __init__(self, contact_id=None):
        """Initializes the ContactsCreate form."""
        super().__init__()
        self.ui = Ui_contacts_create()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()

        # ✅ Connect buttons
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.save_contact)

        # ✅ Load existing contact details if updating
        self.contact_id = contact_id
        if self.contact_id:
            self.load_contact_details()

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def save_contact(self):
        """Saves a new contact, ensuring related data is handled correctly."""
        first_name = self.ui.firstname_line.text().strip()
        last_name = self.ui.lastname_line.text().strip()
        email = self.ui.email_line.text().strip()
        phone_number = self.ui.phone_line.text().strip()
        gender = self.ui.gender_combo.currentText().strip()
        job_title = self.ui.title_line.text().strip()

        # ✅ New Fields
        source_name = self.ui.source_name_line.text().strip()  # Lead Source
        company_name = self.ui.company_line.text().strip()
        company_email = self.ui.company_email_line.text().strip()
        company_website = self.ui.company_website_line.text().strip()
        company_industry = self.ui.company_industry_line.text().strip()

        # ✅ Company Address Fields (with `company_` prefix)
        company_street = self.ui.company_street_line.text().strip()
        company_city = self.ui.company_city_line.text().strip()
        company_state = self.ui.company_state_line.text().strip()
        company_zip_code = self.ui.company_zip_line.text().strip()
        company_country = self.ui.company_country_line.text().strip()
        address_type = self.ui.address_type_combo.currentText().strip()

        # ✅ Contact Address Fields (without `contact_` prefix)
        contact_street = self.ui.street_line.text().strip()
        contact_city = self.ui.city_line.text().strip()
        contact_state = self.ui.state_line.text().strip()
        contact_zip_code = self.ui.zip_line.text().strip()
        contact_country = self.ui.country_line.text().strip()

        if not first_name or not last_name or not email or not phone_number or not company_name:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, phone, and company are required.")
            return

        # ✅ Check if email already exists
        existing_email_query = "SELECT contact_id FROM contact WHERE email = %s"
        existing_email = self.db_conn.fetch_one(existing_email_query, (email,))
        if existing_email:
            QMessageBox.warning(self, "Duplicate Email", "The email address is already associated with an existing contact.")
            return

        # ✅ Ensure `lead_source` exists
        source_query = "SELECT source_id FROM lead_source WHERE source_name = %s"
        source = self.db_conn.fetch_one(source_query, (source_name,))

        if not source and source_name:
            self.db_conn.execute_query("INSERT INTO lead_source (source_name) VALUES (%s)", (source_name,))
            source = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS source_id")

        source_id = source["source_id"] if source else None

        # ✅ Ensure `company` exists
        company_query = "SELECT company_id FROM company WHERE company_name = %s"
        company = self.db_conn.fetch_one(company_query, (company_name,))

        if not company:
            self.db_conn.execute_query(
                "INSERT INTO company (company_name, company_email, website, industry) VALUES (%s, %s, %s, %s)",
                (company_name, company_email, company_website, company_industry)
            )
            company = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_id")

        company_id = company["company_id"]

        # ✅ Insert company_address
        company_address_query = """
            INSERT INTO company_address (company_id, address_type, street, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        company_address_params = (company_id, address_type, company_street, company_city, company_state, company_zip_code, company_country)
        self.db_conn.execute_query(company_address_query, company_address_params)

        # ✅ Retrieve `company_address_id`
        company_address_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_address_id")["company_address_id"]

        # ✅ Insert contact
        contact_query = """
            INSERT INTO contact (first_name, last_name, email, phone_number, gender, job_title, company_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        contact_params = (first_name, last_name, email, phone_number, gender, job_title, company_id)
        self.db_conn.execute_query(contact_query, contact_params)

        # ✅ Retrieve `contact_id`
        contact_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS contact_id")["contact_id"]

        if not contact_id:
            QMessageBox.warning(self, "Error", "Failed to save contact information.")
            return

        # ✅ Insert into `leads` table (if source exists)
        if source_id:
            lead_query = """
                INSERT INTO leads (company_id, contact_id, source_id)
                VALUES (%s, %s, %s)
            """
            lead_params = (company_id, contact_id, source_id)
            self.db_conn.execute_query(lead_query, lead_params)

        # ✅ Insert contact_address
        contact_address_query = """
            INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        contact_address_params = (contact_id, contact_street, contact_city, contact_state, contact_zip_code, contact_country)
        self.db_conn.execute_query(contact_address_query, contact_address_params)

        QMessageBox.information(self, "Success", "Contact saved successfully!")
        self.go_back()
