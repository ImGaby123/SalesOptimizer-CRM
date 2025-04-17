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

class ContactsView(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.ui = Ui_contacts_update()  # Setup the UI components
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()  # Database connection
        self.contact_id = contact_id  # Contact ID to update

        self.setup_country_city_combos()
        self.load_contact_details()

    def set_combo_value(self, combo: QComboBox, value: str, fallback_options=None):
        """Safely sets a value in a combo box, adding it if it's not already present."""
        if fallback_options:
            combo.clear()
            combo.addItems(fallback_options)

        if value and combo.findText(value) == -1:
            combo.addItem(value)
        combo.setCurrentText(value)

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

        # Set basic contact info
        self.ui.firstname_line.setText(contact.get("first_name", ""))
        self.ui.lastname_line.setText(contact.get("last_name", ""))
        self.ui.email_line.setText(contact.get("email", ""))
        self.ui.phone_line.setText(contact.get("phone_number", ""))
        self.ui.gender_combo.setCurrentText(contact.get("gender", ""))
        self.ui.title_combo.setCurrentText(contact.get("job_title", ""))

        # Set address info
        self.ui.street_line.setText(contact.get("street", ""))

        # Set country combo (For viewing)
        contact_country = contact.get("country", "")
        self.set_combo_value(self.ui.country_combo, contact_country, list(country_city_map.keys()))

        # Update city combo based on country (For viewing)
        self.update_city_combo()

        # Set city combo (For viewing)
        contact_city = contact.get("city", "")
        self.ui.city_combo.setCurrentText(contact_city)

        # Set address state and zip
        self.ui.state_line.setText(contact.get("state", ""))
        self.ui.zip_line.setText(contact.get("zip_code", ""))

        # Set company info
        self.ui.company_line.setText(contact.get("company_name", ""))
        self.ui.company_email_line.setText(contact.get("company_email", ""))
        self.ui.company_website_line.setText(contact.get("website", ""))
        self.ui.company_industry_combo.setCurrentText(contact.get("industry", ""))

        # Set years in industry (Make sure this is not None)
        yrs_in_industry = contact.get("yrs_in_industry", "")
        self.ui.yrs_in_industry_line.setText(str(yrs_in_industry) if yrs_in_industry else "")

        # Set lead source
        self.ui.source_name_line.setText(contact.get("lead_source", ""))

        # Set company address fields
        self.ui.company_street_line.setText(contact.get("company_street", ""))
        company_country = contact.get("company_country", "")
        company_city = contact.get("company_city", "")

        # Set company country combo
        self.set_combo_value(self.ui.company_country_combo, company_country, list(country_city_map.keys()))

        # Update company city combo based on company country
        self.update_company_city_combo()

        # Set company city combo
        self.ui.company_city_combo.setCurrentText(company_city)

        # Set company address state and zip
        self.ui.company_state_line.setText(contact.get("company_state", ""))
        self.ui.company_zip_line.setText(contact.get("company_zip_code", ""))

        # Set company address type (Make sure it's set)
        address_type = contact.get("company_address_type", "")
        if address_type:
            self.ui.address_type_combo.setCurrentText(address_type)
        else:
            self.ui.address_type_combo.setCurrentIndex(0)
