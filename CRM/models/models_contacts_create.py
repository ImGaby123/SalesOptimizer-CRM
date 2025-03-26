from PySide6.QtWidgets import QWidget, QMessageBox
from views.py.ui_contacts_create import Ui_contacts_create
from datas.db_connection import DB_Connection

class ContactsCreate(QWidget):
    def __init__(self, contact_id=None):
        """
        Initializes the ContactsCreate form.
        If `contact_id` is provided, fetch the contact details including company name.
        """
        super().__init__()
        self.ui = Ui_contacts_create()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()

        # ✅ Connect buttons
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.save_contact)

        # ✅ Load existing contact details if contact_id is provided
        self.contact_id = contact_id
        if self.contact_id:
            self.load_contact_details()

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def save_contact(self):
        """Saves contact and ensures address is linked."""
        first_name = self.ui.firstname_line.text().strip()
        last_name = self.ui.lastname_line.text().strip()
        email = self.ui.email_line.text().strip()
        phone_number = self.ui.phone_line.text().strip()
        gender = self.ui.gender_combo.currentText().strip()
        job_title = self.ui.title_line.text().strip()  # ✅ Added Job Title

        street = self.ui.street_line.text().strip()
        city = self.ui.city_line.text().strip()
        state = self.ui.state_line.text().strip()
        zip_code = self.ui.zip_line.text().strip()
        country = self.ui.country_line.text().strip()

        company_name = self.ui.company_line.text().strip()

        if not first_name or not last_name or not email or not phone_number or not company_name:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, phone, and company are required.")
            return

        # ✅ Ensure company exists
        company_query = "SELECT company_id FROM company WHERE company_name = %s"
        company = self.db_conn.fetch_one(company_query, (company_name,))

        if not company:
            self.db_conn.execute_query("INSERT INTO company (company_name) VALUES (%s)", (company_name,))
            company = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_id")

        company_id = company["company_id"]

        # ✅ Insert into `contact` table with job title
        contact_query = """
            INSERT INTO contact (first_name, last_name, email, phone_number, gender, job_title, company_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        contact_params = (first_name, last_name, email, phone_number, gender, job_title, company_id)
        self.db_conn.execute_query(contact_query, contact_params)

        # ✅ Retrieve `contact_id`
        contact_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS contact_id")["contact_id"]

        # ✅ Insert into `contact_address` table
        address_query = """
            INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        address_params = (contact_id, street, city, state, zip_code, country)
        self.db_conn.execute_query(address_query, address_params)

        QMessageBox.information(self, "Success", "Contact saved successfully!")
        self.go_back()
