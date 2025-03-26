from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QDate
from views.py.ui_contacts_update import Ui_contacts_update
from datas.db_connection import DB_Connection

class ContactsUpdate(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.ui = Ui_contacts_update()
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()
        self.contact_id = contact_id
        self.load_contact_details()

        # ✅ Connect Save Button
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.update_contact)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        """Fetches and displays contact details (Including Address & Gender)."""
        query = """
        SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender, c.job_title,
               a.street, a.city, a.state, a.zip_code, a.country,
               COALESCE(comp.company_name, '') AS company_name
        FROM contact c
        LEFT JOIN contact_address a ON c.contact_id = a.contact_id
        LEFT JOIN company comp ON c.company_id = comp.company_id
        WHERE c.contact_id = %s
        """

        contact = self.db_conn.fetch_one(query, (self.contact_id,))
        if contact:
            self.ui.firstname_line.setText(contact.get("first_name", ""))
            self.ui.lastname_line.setText(contact.get("last_name", ""))
            self.ui.email_line.setText(contact.get("email", ""))
            self.ui.phone_line.setText(contact.get("phone_number", ""))
            self.ui.gender_combo.setCurrentText(contact.get("gender", ""))
            self.ui.title_line.setText(contact.get("job_title", ""))
            self.ui.street_line.setText(contact.get("street", ""))
            self.ui.city_line.setText(contact.get("city", ""))
            self.ui.state_line.setText(contact.get("state", ""))
            self.ui.zip_line.setText(contact.get("zip_code", ""))
            self.ui.country_line.setText(contact.get("country", ""))
            self.ui.company_line.setText(contact.get("company_name", ""))

    def update_contact(self):
        """Updates contact, address, and company information."""
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

        if not first_name or not last_name or not email or not phone_number:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, and phone number are required.")
            return

        # ✅ Update `contact` table
        contact_query = """
        UPDATE contact SET first_name=%s, last_name=%s, email=%s, phone_number=%s, gender=%s, job_title=%s
        WHERE contact_id=%s
        """
        contact_params = (first_name, last_name, email, phone_number, gender, job_title, self.contact_id)
        self.db_conn.execute_query(contact_query, contact_params)

        # ✅ Check if address exists
        check_address = self.db_conn.fetch_one("SELECT * FROM contact_address WHERE contact_id = %s", (self.contact_id,))

        if check_address:
            address_query = """
                UPDATE contact_address SET street=%s, city=%s, state=%s, zip_code=%s, country=%s
                WHERE contact_id=%s
            """
        else:
            address_query = """
                INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

        address_params = (street, city, state, zip_code, country, self.contact_id)
        self.db_conn.execute_query(address_query, address_params)

        # ✅ Update `company`
        if company_name:
            company_query = "SELECT company_id FROM company WHERE company_name = %s"
            company = self.db_conn.fetch_one(company_query, (company_name,))

            if company:
                company_id = company["company_id"]
            else:
                # Insert new company if not found
                self.db_conn.execute_query("INSERT INTO company (company_name) VALUES (%s)", (company_name,))
                company_id = self.db_conn.fetch_one("SELECT company_id FROM company WHERE company_name = %s", (company_name,))["company_id"]

            # ✅ Update `contact` with new `company_id`
            update_company_query = "UPDATE contact SET company_id = %s WHERE contact_id = %s"
            self.db_conn.execute_query(update_company_query, (company_id, self.contact_id))

        QMessageBox.information(self, "Success", "Contact updated successfully!")
        self.go_back()
