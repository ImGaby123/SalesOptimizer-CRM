from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit
from views.py.ui_contacts_create import Ui_contacts_create
from datas.db_connection import DB_Connection
import re

class ContactsCreate(QWidget):
    def __init__(self, contact_id=None):
        super().__init__()
        self.ui = Ui_contacts_create()
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()

        self.validation_rules()
        self.country_city_setup()

        self.ui.back_line.clicked.connect(self.go_back)
        self.ui.save_btn.clicked.connect(self.save_contact)
        self.ui.country_combo.currentTextChanged.connect(self.toggle_city_combo)
        self.ui.company_country_combo.currentTextChanged.connect(self.toggle_company_city_combo)

        self.contact_id = contact_id
        if self.contact_id:
            self.load_contact_details()

    def validation_rules(self):
        self.letters_only = re.compile(r"^[a-zA-Z\s]+$")
        self.alpha_numeric = re.compile(r"^[\w\s\-.,@:/]+$")
        self.three_digits = re.compile(r"^\d{1,3}$")
        self.email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
        self.phone_validation = re.compile(r"^\+?[\d\s\-()]{7,20}$")

    def show_invalid_message(self, field_name):
        QMessageBox.warning(self, "Invalid Input", f"The input for '{field_name}' is invalid.")

    def validate_field(self, value, regex, field_name):
        if value and not regex.match(value):
            self.show_invalid_message(field_name)
            return False
        return True

    def country_city_setup(self):
        self.country_city_map = {
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

        self.ui.country_combo.addItems(self.country_city_map.keys())
        self.ui.company_country_combo.addItems(self.country_city_map.keys())
        self.ui.city_combo.setEnabled(False)
        self.ui.company_city_combo.setEnabled(False)

    def toggle_city_combo(self, country):
        self.ui.city_combo.clear()
        cities = self.country_city_map.get(country)
        if cities:
            self.ui.city_combo.addItems(cities)
            self.ui.city_combo.setEnabled(True)
        else:
            self.ui.city_combo.setEnabled(False)

    def toggle_company_city_combo(self, country):
        self.ui.company_city_combo.clear()
        cities = self.country_city_map.get(country)
        if cities:
            self.ui.company_city_combo.addItems(cities)
            self.ui.company_city_combo.setEnabled(True)
        else:
            self.ui.company_city_combo.setEnabled(False)

    def go_back(self):
        from models.models_authentication import MDIManager
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        query = "SELECT * FROM contact WHERE contact_id = %s"
        contact = self.db_conn.fetch_one(query, (self.contact_id,))
        if contact:
            self.ui.firstname_line.setText(contact["first_name"])
            self.ui.lastname_line.setText(contact["last_name"])
            self.ui.email_line.setText(contact["email"])
            self.ui.phone_line.setText(contact["phone_number"])
            self.ui.gender_combo.setCurrentText(contact["gender"])
            self.ui.title_combo.setCurrentText(contact["job_title"])

    def save_contact(self):
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

        # Required field check
        if not first_name or not last_name or not email or not phone_number or not company_name or not company_email:
            QMessageBox.warning(self, "Missing Fields", "First name, last name, email, phone, company and company_email are required.")
            return

        # Manual validation
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

        existing_email = self.db_conn.fetch_one("SELECT contact_id FROM contact WHERE email = %s", (email,))
        if existing_email:
            QMessageBox.warning(self, "Duplicate Email", "The email address is already associated with an existing contact.")
            return

        source = self.db_conn.fetch_one("SELECT source_id FROM lead_source WHERE source_name = %s", (source_name,))
        if not source and source_name:
            self.db_conn.execute_query("INSERT INTO lead_source (source_name) VALUES (%s)", (source_name,))
            source = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS source_id")
        source_id = source["source_id"] if source else None

        company = self.db_conn.fetch_one("SELECT company_id FROM company WHERE company_email = %s", (company_email,))
        if company:
            QMessageBox.warning(self, "Duplicate Company Email", "A company with this email already exists.")
            return

        company = self.db_conn.fetch_one("SELECT company_id FROM company WHERE company_name = %s", (company_name,))
        if not company:
            self.db_conn.execute_query(
                "INSERT INTO company (company_name, company_email, website, industry, yrs_in_industry) VALUES (%s, %s, %s, %s, %s)",
                (company_name, company_email, company_website, company_industry, yrs_in_industry)
            )
            company = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_id")
        company_id = company["company_id"]

        self.db_conn.execute_query("""
            INSERT INTO company_address (company_id, address_type, street, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (company_id, address_type, company_street, company_city, company_state, company_zip_code, company_country))

        company_address_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS company_address_id")["company_address_id"]

        self.db_conn.execute_query("""
            INSERT INTO contact (first_name, last_name, email, phone_number, gender, job_title, company_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, phone_number, gender, job_title, company_id))

        contact_id = self.db_conn.fetch_one("SELECT LAST_INSERT_ID() AS contact_id")["contact_id"]
        if not contact_id:
            QMessageBox.warning(self, "Error", "Failed to save contact information.")
            return

        if source_id:
            self.db_conn.execute_query("""
                INSERT INTO leads (company_id, contact_id, source_id)
                VALUES (%s, %s, %s)
            """, (company_id, contact_id, source_id))

        self.db_conn.execute_query("""
            INSERT INTO contact_address (contact_id, street, city, state, zip_code, country)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (contact_id, contact_street, contact_city, contact_state, contact_zip_code, contact_country))

        QMessageBox.information(self, "Success", "Contact saved successfully!")
        self.go_back()
