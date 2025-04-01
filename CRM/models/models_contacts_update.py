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

        # Connect Buttons
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.update_contact)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        """Fetches and displays contact details, including address, company, and lead source."""
        if not self.db_conn.conn:  # Ensure DB connection exists
            QMessageBox.critical(self, "Database Error", "Unable to connect to the database.")
            return

        query = """
        SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender, c.job_title,
               a.street, a.city, a.state, a.zip_code, a.country,
               ca_comp.street AS company_street, ca_comp.city AS company_city, ca_comp.state AS company_state,
               ca_comp.zip_code AS company_zip_code, ca_comp.country AS company_country,
               ca_comp.address_type AS company_address_type,
               COALESCE(comp.company_name, '') AS company_name,
               comp.company_email, comp.website, comp.industry,
               ls.source_name AS lead_source
        FROM contact c
        LEFT JOIN contact_address a ON c.contact_id = a.contact_id
        LEFT JOIN company comp ON c.company_id = comp.company_id
        LEFT JOIN company_address ca_comp ON comp.company_id = ca_comp.company_id
        LEFT JOIN leads l ON c.contact_id = l.contact_id
        LEFT JOIN lead_source ls ON l.source_id = ls.source_id
        WHERE c.contact_id = %s
        """

        contact = self.db_conn.fetch_one(query, (self.contact_id,))

        if not contact:
            QMessageBox.warning(self, "Not Found", "The requested contact does not exist.")
            self.go_back()
            return

        # Set text safely (preventing NoneType errors)
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
        self.ui.company_email_line.setText(contact.get("company_email", ""))
        self.ui.company_website_line.setText(contact.get("website", ""))
        self.ui.company_industry_line.setText(contact.get("industry", ""))
        self.ui.source_name_line.setText(contact.get("lead_source", ""))  # Corrected here

        # Set company address fields
        self.ui.company_street_line.setText(contact.get("company_street", ""))
        self.ui.company_city_line.setText(contact.get("company_city", ""))
        self.ui.company_state_line.setText(contact.get("company_state", ""))
        self.ui.company_zip_line.setText(contact.get("company_zip_code", ""))
        self.ui.company_country_line.setText(contact.get("company_country", ""))

        # Set company address type (for company address)
        address_type = contact.get("company_address_type", "")
        if address_type:
            self.ui.address_type_combo.setCurrentText(address_type)
        else:
            self.ui.address_type_combo.setCurrentIndex(0)  # Default to the first option

    def update_contact(self):
        """Updates contact, address, company, and lead source information."""
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
        company_email = self.ui.company_email_line.text().strip()
        website = self.ui.company_website_line.text().strip()
        industry = self.ui.company_industry_line.text().strip()

        # Get company address information
        company_street = self.ui.company_street_line.text().strip()
        company_city = self.ui.company_city_line.text().strip()
        company_state = self.ui.company_state_line.text().strip()
        company_zip_code = self.ui.company_zip_line.text().strip()
        company_country = self.ui.company_country_line.text().strip()
        address_type = self.ui.address_type_combo.currentText().strip()

        lead_source = self.ui.source_name_line.text().strip()  # Corrected here

        if not first_name or not last_name or not email or not phone_number:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, and phone number are required.")
            return

        if not self.db_conn.conn:  # Ensure DB connection exists
            QMessageBox.critical(self, "Database Error", "Database connection is unavailable.")
            return

        # Update `contact` table
        contact_query = """
        UPDATE contact
        SET first_name=%s, last_name=%s, email=%s, phone_number=%s, gender=%s, job_title=%s
        WHERE contact_id=%s
        """
        contact_params = (first_name, last_name, email, phone_number, gender, job_title, self.contact_id)
        self.db_conn.execute_query(contact_query, contact_params)

        # Update or insert contact address
        check_address = self.db_conn.fetch_one("SELECT 1 FROM contact_address WHERE contact_id = %s", (self.contact_id,))

        if check_address:
            address_query = """
                UPDATE contact_address
                SET street=%s, city=%s, state=%s, zip_code=%s, country=%s
                WHERE contact_id=%s
            """
            address_params = (street, city, state, zip_code, country, self.contact_id)
        else:
            address_query = """
                INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            address_params = (self.contact_id, street, city, state, zip_code, country)

        self.db_conn.execute_query(address_query, address_params)

        # Update or Insert `company`
        if company_name:
            company_query = "SELECT company_id FROM company WHERE company_name = %s"
            company = self.db_conn.fetch_one(company_query, (company_name,))

            if company:
                company_id = company["company_id"]
                update_company_query = """
                    UPDATE company
                    SET company_email=%s, website=%s, industry=%s
                    WHERE company_id=%s
                """
                self.db_conn.execute_query(update_company_query, (company_email, website, industry, company_id))
            else:
                # Insert new company if not found
                self.db_conn.execute_query("INSERT INTO company (company_name, company_email, website, industry) VALUES (%s, %s, %s, %s)",
                                            (company_name, company_email, website, industry))
                company_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_id")["company_id"]

            # Update `contact` with new `company_id`
            update_company_query = "UPDATE contact SET company_id = %s WHERE contact_id = %s"
            self.db_conn.execute_query(update_company_query, (company_id, self.contact_id))

            # Update or Insert `company_address`
            company_address_query = """
                SELECT company_address_id FROM company_address WHERE company_id = %s
            """
            company_address = self.db_conn.fetch_one(company_address_query, (company_id,))

            if company_address:
                # Update company address
                company_address_update_query = """
                    UPDATE company_address
                    SET street=%s, city=%s, state=%s, zip_code=%s, country=%s, address_type=%s
                    WHERE company_address_id=%s
                """
                company_address_params = (company_street, company_city, company_state, company_zip_code, company_country, address_type, company_address["company_address_id"])
                self.db_conn.execute_query(company_address_update_query, company_address_params)
            else:
                # Insert new company address
                company_address_insert_query = """
                    INSERT INTO company_address (company_id, street, city, state, zip_code, country, address_type)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                company_address_params = (company_id, company_street, company_city, company_state, company_zip_code, company_country, address_type)
                self.db_conn.execute_query(company_address_insert_query, company_address_params)

        # Update or Insert Lead Source
        if lead_source:
            lead_source_query = "SELECT source_id FROM lead_source WHERE source_name = %s"
            lead_source_record = self.db_conn.fetch_one(lead_source_query, (lead_source,))

            if lead_source_record:
                lead_source_id = lead_source_record["source_id"]
            else:
                # Insert new lead source if not found
                self.db_conn.execute_query("INSERT INTO lead_source (source_name) VALUES (%s)", (lead_source,))
                lead_source_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS source_id")["source_id"]

            # Update or Insert `leads` table with lead_source_id
            update_lead_query = """
                UPDATE leads
                SET source_id = %s
                WHERE contact_id = %s
            """
            self.db_conn.execute_query(update_lead_query, (lead_source_id, self.contact_id))

        QMessageBox.information(self, "Success", "Contact updated successfully!")
        self.go_back()
