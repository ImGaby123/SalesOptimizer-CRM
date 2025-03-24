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
        """Fetches contact details and populates UI fields."""
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
            dob = contact.get("date_of_birth", None)
            if dob:
                self.ui.dob_date.setDate(QDate.fromString(str(dob), "yyyy-MM-dd"))
            else:
                self.ui.dob_date.setDate(QDate.currentDate())  # Default to today if no DOB

            self.ui.title_line.setText(contact.get("job_title", ""))
            self.ui.email_line.setText(contact.get("email", ""))
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
            self.ui.comany_line.setText(contact.get("company_name", ""))

    def update_contact(self):
        """Updates the contact information in the database."""
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

        # ✅ Ensure required fields are not empty
        if not first_name or not last_name or not email or not phone_number:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, and phone number are required.")
            return

        # ✅ Update `contact` table
        contact_query = """
        UPDATE contact SET first_name=%s, last_name=%s, middle_name=%s, suffix=%s,
                           date_of_birth=%s, job_title=%s, email=%s, phone_number=%s
        WHERE contact_id=%s
        """
        contact_params = (first_name, last_name, middle_name, suffix, date_of_birth, job_title, email, phone_number, self.contact_id)
        success_contact = self.db_conn.execute_query(contact_query, contact_params)

        # ✅ Update `info` table
        info_query = """
        UPDATE info SET secondary_email=%s, other_phone_number=%s, gender=%s, fax=%s
        WHERE contact_id=%s
        """
        info_params = (secondary_email, other_phone_number, gender, fax, self.contact_id)
        success_info = self.db_conn.execute_query(info_query, info_params)

        # ✅ Update `address` table
        address_query = """
        UPDATE address SET country=%s, state=%s, city=%s, street=%s, postal_code=%s
        WHERE contact_id=%s
        """
        address_params = (country, state, city, street, postal_code, self.contact_id)
        success_address = self.db_conn.execute_query(address_query, address_params)

        # ✅ Update `company` (If company is provided)
        success_owner = True
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
                # Fetch the new company ID
                company_id = self.db_conn.fetch_one("SELECT company_id FROM company WHERE company_name = %s", (company_name,))["company_id"]

            # ✅ Update `owner` table
            owner_query = """
            INSERT INTO owner (contact_owner_id, company_id) VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE company_id = VALUES(company_id)
            """
            owner_params = (self.contact_id, company_id)
            success_owner = self.db_conn.execute_query(owner_query, owner_params)

        # ✅ Check if all updates were successful
        if success_contact and success_info and success_address and success_owner:
            QMessageBox.information(self, "Success", "Contact updated successfully!")
        else:
            QMessageBox.critical(self, "Error", "Failed to update contact. Please try again.")
