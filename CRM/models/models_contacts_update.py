from PySide6.QtWidgets import QWidget, QMessageBox, QComboBox
from PySide6.QtCore import QDate
from views.py.ui_contacts_update import Ui_contacts_update
from datas.db_connection import DB_Connection
import re

# Country-City Mapping
country_city_map = {
    "Philippines": ["Quezon City", "Manila", "Makati", "Cebu City", "Davao City", "Taguig", "Pasig", "Baguio", "Iloilo City", "Cagayan de Oro"],
    "United States": ["New York", "Los Angeles", "Chicago"],
    "Canada": ["Toronto", "Vancouver", "Montreal"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"],
    "Germany": ["Berlin", "Munich", "Frankfurt"],
    "France": ["Paris", "Lyon", "Marseille"],
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "China": ["Beijing", "Shanghai", "Guangzhou"],
    "Brazil": ["São Paulo", "Rio de Janeiro", "Brasília"],
    "South Africa": ["Johannesburg", "Cape Town", "Durban"],
    "United Arab Emirates": ["Dubai", "Abu Dhabi", "Sharjah"],
    "Singapore": ["Singapore"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"],
    "Mexico": ["Mexico City", "Guadalajara", "Monterrey"],
    "Netherlands": ["Amsterdam", "Rotterdam", "The Hague"],
    "Others": ["Other City 1", "Other City 2", "Other City 3"]
}

class ContactsUpdate(QWidget):
    def __init__(self, contact_id):
        """Initialize the Contacts Update form."""
        super().__init__()
        self.ui = Ui_contacts_update()  # Setup the UI components
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()  # Database connection
        self.contact_id = contact_id  # Contact ID to update

        self.setup_country_city_combos()
        self.load_contact_details()

        # Connect UI buttons to methods
        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.update_contact)

        # Set up the validation rules
        self.validation_rules()

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)  # Loads the ContactsLanding form

    def load_contact_details(self):
        """Fetches and displays contact details from the database."""
        if not self.db_conn.conn:
            QMessageBox.critical(self, "Database Error", "Unable to connect to the database.")
            return

        query = """
        SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender, c.job_title,
               a.street, a.city, a.state, a.zip_code, a.country,
               ca_comp.street AS company_street, ca_comp.city AS company_city, ca_comp.state AS company_state,
               ca_comp.zip_code AS company_zip_code, ca_comp.country AS company_country,
               ca_comp.address_type AS company_address_type,
               COALESCE(comp.company_name, '') AS company_name,
               comp.company_email, comp.website, comp.industry, comp.yrs_in_industry,
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

        # Basic contact info
        self.ui.firstname_line.setText(contact.get("first_name", ""))
        self.ui.lastname_line.setText(contact.get("last_name", ""))
        self.ui.email_line.setText(contact.get("email", ""))
        self.ui.phone_line.setText(contact.get("phone_number", ""))
        self.ui.gender_combo.setCurrentText(contact.get("gender", ""))
        self.ui.title_combo.setCurrentText(contact.get("job_title", ""))

        # Contact address
        self.ui.street_line.setText(contact.get("street", ""))
        contact_country = contact.get("country", "")
        contact_city = contact.get("city", "")
        self.set_combo_value(self.ui.country_combo, contact_country, list(country_city_map.keys()))
        self.update_city_combo()
        if self.ui.city_combo.findText(contact_city) == -1:
            self.ui.city_combo.addItem(contact_city)
        self.ui.city_combo.setCurrentText(contact_city)
        self.ui.state_line.setText(contact.get("state", ""))
        self.ui.zip_line.setText(contact.get("zip_code", ""))

        # Company info
        self.ui.company_line.setText(contact.get("company_name", ""))
        self.ui.company_email_line.setText(contact.get("company_email", ""))
        self.ui.company_website_line.setText(contact.get("website", ""))
        self.ui.company_industry_combo.setCurrentText(contact.get("industry", ""))
        self.ui.yrs_in_industry_line.setText(str(contact.get("yrs_in_industry", "")))
        self.ui.source_name_line.setText(contact.get("lead_source", ""))

        # Company address
        self.ui.company_street_line.setText(contact.get("company_street", ""))
        company_country = contact.get("company_country", "")
        company_city = contact.get("company_city", "")
        self.set_combo_value(self.ui.company_country_combo, company_country, list(country_city_map.keys()))
        self.update_company_city_combo()
        if self.ui.company_city_combo.findText(company_city) == -1:
            self.ui.company_city_combo.addItem(company_city)
        self.ui.company_city_combo.setCurrentText(company_city)
        self.ui.company_state_line.setText(contact.get("company_state", ""))
        self.ui.company_zip_line.setText(contact.get("company_zip_code", ""))

        # Company address type
        address_type = contact.get("company_address_type", "")
        if address_type:
            self.ui.address_type_combo.setCurrentText(address_type)
        else:
            self.ui.address_type_combo.setCurrentIndex(0)


    def set_combo_value(self, combo: QComboBox, value: str, fallback_options=None):
        """Safely sets a value in a combo box, adding it if it's not already present."""
        if fallback_options:
            combo.clear()
            combo.addItems(fallback_options)

        if value and combo.findText(value) == -1:
            combo.addItem(value)
        combo.setCurrentText(value)

    def validation_rules(self):
        """Set validation rules for different fields."""
        self.letters_only = re.compile(r"^[a-zA-Z\s]+$")
        self.alpha_numeric = re.compile(r"^[\w\s\-.,@:/]+$")
        self.three_digits = re.compile(r"^\d{1,3}$")
        self.email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        self.phone_validation = re.compile(r"^\+?[\d\s\-()]{7,20}$")

    def show_invalid_message(self, field_name):
        """Show message box for invalid fields."""
        QMessageBox.warning(self, "Invalid Input", f"The input for '{field_name}' is invalid.")

    def validate_field(self, value, regex, field_name):
        """Validate individual fields."""
        if value and not regex.match(value):
            self.show_invalid_message(field_name)
            return False
        return True

    def setup_country_city_combos(self):
        """Set up country-city combo box mapping."""
        self.ui.country_combo.addItems(country_city_map.keys())
        self.ui.company_country_combo.addItems(country_city_map.keys())

        # Disable city combo boxes initially
        self.ui.city_combo.setEnabled(False)
        self.ui.company_city_combo.setEnabled(False)

        # Set the corresponding cities based on selected country
        self.ui.country_combo.currentTextChanged.connect(self.update_city_combo)
        self.ui.company_country_combo.currentTextChanged.connect(self.update_company_city_combo)

    def update_city_combo(self):
        """Update city combo based on selected country."""
        country = self.ui.country_combo.currentText()
        if country:
            cities = country_city_map.get(country, [])
            self.ui.city_combo.clear()
            self.ui.city_combo.addItems(cities)
            self.ui.city_combo.setEnabled(True)
        else:
            self.ui.city_combo.setEnabled(False)

    def update_company_city_combo(self):
        """Update company city combo based on selected country."""
        company_country = self.ui.company_country_combo.currentText()
        if company_country:
            cities = country_city_map.get(company_country, [])
            self.ui.company_city_combo.clear()
            self.ui.company_city_combo.addItems(cities)
            self.ui.company_city_combo.setEnabled(True)
        else:
            self.ui.company_city_combo.setEnabled(False)

    def update_contact(self):
        """Updates contact, address, company, and lead source information."""
        first_name = self.ui.firstname_line.text().strip()
        last_name = self.ui.lastname_line.text().strip()
        email = self.ui.email_line.text().strip()
        phone_number = self.ui.phone_line.text().strip()
        gender = self.ui.gender_combo.currentText().strip()
        job_title = self.ui.title_combo.currentText().strip()

        source_name = self.ui.source_name_line.text().strip()
        company_name = self.ui.company_line.text().strip()
        company_email = self.ui.company_email_line.text().strip()
        company_website = self.ui.company_website_line.text().strip()
        company_industry = self.ui.company_industry_combo.currentText().strip()
        yrs_in_industry = self.ui.yrs_in_industry_line.text().strip()

        company_street = self.ui.company_street_line.text().strip()
        company_city = self.ui.company_city_combo.currentText().strip()
        company_state = self.ui.company_state_line.text().strip()
        company_zip_code = self.ui.company_zip_line.text().strip()
        company_country = self.ui.company_country_combo.currentText().strip()
        address_type = self.ui.address_type_combo.currentText().strip()

        contact_street = self.ui.street_line.text().strip()
        contact_city = self.ui.city_combo.currentText().strip()
        contact_state = self.ui.state_line.text().strip()
        contact_zip_code = self.ui.zip_line.text().strip()
        contact_country = self.ui.country_combo.currentText().strip()

        # Perform validation
        validations = [
            (first_name, self.letters_only, "First Name"),
            (last_name, self.letters_only, "Last Name"),
            (source_name, self.letters_only, "Lead Source"),
            (contact_street, self.letters_only, "Street"),
            (contact_state, self.letters_only, "State"),
            (company_street, self.letters_only, "Company Street"),
            (company_state, self.letters_only, "Company State"),
            (phone_number, self.phone_validation, "Phone Number"),
            (yrs_in_industry, self.three_digits, "Years in Industry"),
            (contact_zip_code, self.alpha_numeric, "Zip Code"),
            (company_zip_code, self.alpha_numeric, "Company Zip"),
            (company_website, self.alpha_numeric, "Website"),
            (email, self.email_regex, "Email"),
            (company_email, self.email_regex, "Company Email")
        ]

        for val, pattern, label in validations:
            if not self.validate_field(val, pattern, label):
                return

        if not self.db_conn.conn:  # Ensure DB connection exists
            QMessageBox.critical(self, "Database Error", "Database connection is unavailable.")
            return

        # Update contact information
        self.db_conn.execute_query("""
            UPDATE contact
            SET first_name = %s, last_name = %s, email = %s, phone_number = %s, gender = %s, job_title = %s
            WHERE contact_id = %s
        """, (first_name, last_name, email, phone_number, gender, job_title, self.contact_id))

        # Update contact address information
        self.db_conn.execute_query("""
            UPDATE contact_address
            SET street = %s, city = %s, state = %s, zip_code = %s, country = %s
            WHERE contact_id = %s
        """, (contact_street, contact_city, contact_state, contact_zip_code, contact_country, self.contact_id))

        # Update company information
        self.db_conn.execute_query("""
            UPDATE company
            SET company_name = %s, company_email = %s, website = %s, industry = %s, yrs_in_industry = %s
            WHERE company_id = (SELECT company_id FROM contact WHERE contact_id = %s)
        """, (company_name, company_email, company_website, company_industry, yrs_in_industry, self.contact_id))

        # Update company address information
        self.db_conn.execute_query("""
            UPDATE company_address
            SET street = %s, city = %s, state = %s, zip_code = %s, country = %s, address_type = %s
            WHERE company_id = (SELECT company_id FROM contact WHERE contact_id = %s)
        """, (company_street, company_city, company_state, company_zip_code, company_country, address_type, self.contact_id))

        # Ensure lead source exists or create it
        existing_source = self.db_conn.fetch_one(
            "SELECT source_id FROM lead_source WHERE source_name = %s", (source_name,)
        )

        if not existing_source:
            # Insert new lead source
            self.db_conn.execute_query(
                "INSERT INTO lead_source (source_name) VALUES (%s)", (source_name,)
        )

        # Now update the leads table
        self.db_conn.execute_query("""
            UPDATE leads
            SET source_id = (SELECT source_id FROM lead_source WHERE source_name = %s)
            WHERE contact_id = %s
        """, (source_name, self.contact_id))

        # Commit the changes and inform the user
        QMessageBox.information(self, "Success", "Contact updated successfully!")
        self.go_back()
