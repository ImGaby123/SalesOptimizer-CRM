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

    def load_contact_details(self):
        """Fetches contact details including company name and populates UI fields."""
        query = """
        SELECT c.first_name, c.last_name, c.middle_name, c.suffix, c.date_of_birth,
               c.job_title, c.email, c.phone_number,
               i.secondary_email, i.other_phone_number, i.gender, i.fax,
               a.country, a.state, a.city, a.street, a.postal_code,
               co.company_name
        FROM contact c
        LEFT JOIN info i ON c.contact_id = i.contact_id
        LEFT JOIN address a ON c.contact_id = a.contact_id
        LEFT JOIN owner o ON c.contact_id = o.contact_owner_id
        LEFT JOIN company co ON o.company_id = co.company_id
        WHERE c.contact_id = %s
        """

        contact = self.db_conn.fetch_one(query, (self.contact_id,))

        if contact:
            self.ui.firstname_line.setText(contact.get("first_name", ""))
            self.ui.lastname_line.setText(contact.get("last_name", ""))
            self.ui.middlename.setText(contact.get("middle_name", ""))
            self.ui.suffix_line.setText(contact.get("suffix", ""))
            date_of_birth = contact.get("date_of_birth", "")
            if date_of_birth:
                qdate = QDate.fromString(date_of_birth, "yyyy-MM-dd")
                self.ui.dob_date.setDate(qdate)
            self.ui.title_line.setText(contact.get("job_title", ""))
            self.ui.email_btn.setText(contact.get("email", ""))
            self.ui.phone_line.setText(contact.get("phone_number", ""))

            self.ui.secondaryemail_line.setText(contact.get("secondary_email", ""))
            self.ui.otherphone_line.setText(contact.get("other_phone_number", ""))
            self.ui.fax_line.setText(contact.get("fax", ""))
            self.ui.gender_combo.setCurrentText(contact.get("gender", ""))

            self.ui.country_line.setText(contact.get("country", ""))
            self.ui.state_line.setText(contact.get("state", ""))
            self.ui.city_line.setText(contact.get("city", ""))
            self.ui.street_line.setText(contact.get("street", ""))
            self.ui.zip_line.setText(contact.get("postal_code", ""))

            # ✅ Set company name in company_line
            self.ui.comany_line.setText(contact.get("company_name", ""))

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def save_contact(self):
        """Saves form data into the database across `contact`, `info`, `address`, and links company."""
        # ✅ Fetch user inputs from form
        first_name = self.ui.firstname_line.text().strip()
        last_name = self.ui.lastname_line.text().strip()
        middle_name = self.ui.middlename.text().strip()
        suffix = self.ui.suffix_line.text().strip()
        date_of_birth = self.ui.dob_date.date().toString("yyyy-MM-dd")
        job_title = self.ui.title_line.text().strip()
        email = self.ui.email_line.text().strip()
        phone_number = self.ui.phone_line.text().strip()

        secondary_email = self.ui.secondaryemail_line.text().strip()
        other_phone_number = self.ui.otherphone_line.text().strip()
        gender = self.ui.gender_combo.currentText().strip()
        fax = self.ui.fax_line.text().strip()

        country = self.ui.country_line.text().strip()
        state = self.ui.state_line.text().strip()
        city = self.ui.city_line.text().strip()
        street = self.ui.street_line.text().strip()
        postal_code = self.ui.zip_line.text().strip()

        company_name = self.ui.comany_line.text().strip()

        # ✅ Validate required fields
        if not first_name or not last_name or not email or not phone_number or not company_name:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, phone number, and company are required.")
            return

        # ✅ Insert into `contact` table
        contact_query = """
            INSERT INTO contact (first_name, last_name, middle_name, suffix, date_of_birth,
                                 job_title, email, phone_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        contact_params = (first_name, last_name, middle_name, suffix, date_of_birth, job_title, email, phone_number)
        if not self.db_conn.execute_query(contact_query, contact_params):
            QMessageBox.critical(self, "Error", "Failed to save contact.")
            return

        # ✅ Retrieve the last inserted `contact_id`
        contact_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID()")["LAST_INSERT_ID()"]

        # ✅ Insert into `info` table
        info_query = """
            INSERT INTO info (contact_id, secondary_email, other_phone_number, gender, fax)
            VALUES (%s, %s, %s, %s, %s)
        """
        info_params = (contact_id, secondary_email, other_phone_number, gender, fax)
        self.db_conn.execute_query(info_query, info_params)

        # ✅ Insert into `address` table
        address_query = """
            INSERT INTO address (contact_id, country, state, city, street, postal_code)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        address_params = (contact_id, country, state, city, street, postal_code)
        self.db_conn.execute_query(address_query, address_params)

        # ✅ Handle company association
        if company_name:
            # Check if company already exists
            company_query = "SELECT company_id FROM company WHERE company_name = %s"
            company = self.db_conn.fetch_one(company_query, (company_name,))

            if company:
                company_id = company["company_id"]
            else:
                # Insert new company
                insert_company_query = "INSERT INTO company (company_name) VALUES (%s)"
                self.db_conn.execute_query(insert_company_query, (company_name,))
                company_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID()")["LAST_INSERT_ID()"]

            # ✅ Insert into `owner` table (linking contact to company)
            owner_query = "INSERT INTO owner (contact_owner_id, company_id) VALUES (%s, %s)"
            self.db_conn.execute_query(owner_query, (contact_id, company_id))

        QMessageBox.information(self, "Success", "Contact saved successfully!")
        self.go_back()  # Redirect user back to the contact list after saving
