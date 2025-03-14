from PySide6.QtWidgets import QWidget, QMessageBox
from views.py.ui_contacts_create import Ui_contacts_create
from datas.db_connection import Database

class ContactsCreate(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts_create()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = Database()

        # ✅ Connect buttons
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.save_contact)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def save_contact(self):
        """Saves form data into the database across `contact`, `info`, and `address` tables."""
        # ✅ Fetch user inputs from form
        first_name = self.ui.firstname_line.text().strip()
        last_name = self.ui.lastname_line.text().strip()
        middle_name = self.ui.middlename.text().strip()
        suffix = self.ui.suffix_line.text().strip()
        date_of_birth = self.ui.dateofbirth_btn.text().strip()
        job_title = self.ui.title_line.text().strip()
        email = self.ui.email_btn.text().strip()
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

        # ✅ Validate required fields
        if not first_name or not last_name or not email:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, and email are required.")
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

        QMessageBox.information(self, "Success", "Contact saved successfully!")
        self.go_back()  # Redirect user back to the contact list after saving
