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
        job_title = self.ui.title_line.text().strip()

        street = self.ui.street_line.text().strip()
        city = self.ui.city_line.text().strip()
        state = self.ui.state_line.text().strip()
        zip_code = self.ui.zip_line.text().strip()
        country = self.ui.country_line.text().strip()

        company_name = self.ui.company_line.text().strip()

        if not first_name or not last_name or not email or not phone_number or not company_name:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, phone, and company are required.")
            return

        self.db_conn.ensure_connection()
        conn = self.db_conn.conn
        cursor = conn.cursor(dictionary=True)

        try:
            conn.start_transaction()

            # ✅ Prevent duplicate company entries
            cursor.execute(
                "SELECT company_id FROM company WHERE company_name = %s LIMIT 1",
                (company_name,)
            )
            company = cursor.fetchone()

            if not company:
                cursor.execute("INSERT INTO company (company_name) VALUES (%s)", (company_name,))
                company_id = cursor.lastrowid  # Get new company_id
            else:
                company_id = company["company_id"]

            # ✅ Prevent duplicate contacts (email must be unique)
            cursor.execute("SELECT contact_id FROM contact WHERE email = %s LIMIT 1", (email,))
            existing_contact = cursor.fetchone()

            if existing_contact:
                QMessageBox.warning(self, "Duplicate Contact", "A contact with this email already exists.")
                conn.rollback()
                return

            # ✅ Insert contact
            cursor.execute(
                """
                INSERT INTO contact (first_name, last_name, email, phone_number, gender, job_title, company_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (first_name, last_name, email, phone_number, gender, job_title, company_id)
            )
            contact_id = cursor.lastrowid  # Get new contact_id

            # ✅ Insert contact address
            cursor.execute(
                """
                INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (contact_id, street, city, state, zip_code, country)
            )

            conn.commit()
            QMessageBox.information(self, "Success", "Contact saved successfully!")
            self.go_back()

        except Exception as e:
            conn.rollback()
            QMessageBox.critical(self, "Database Error", f"An error occurred: {str(e)}")

        finally:
            cursor.close()
