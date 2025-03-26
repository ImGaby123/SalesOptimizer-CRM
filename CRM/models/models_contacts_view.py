from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate
from views.py.ui_contacts_view import Ui_contacts_view
from datas.db_connection import DB_Connection

class ContactsView(QWidget):  # ✅ Changed from QDialog to QWidget
    def __init__(self, contact_id):
        super().__init__()
        self.ui = Ui_contacts_view()
        self.ui.setupUi(self)

        self.db_conn = DB_Connection()
        self.contact_id = contact_id
        self.load_contact_details()

        self.ui.back_line.clicked.connect(self.go_back)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager  # Lazy import to prevent circular imports
        from models.models_contacts_landing import ContactsLanding
        MDIManager.load_into_mdi(ContactsLanding)

    def load_contact_details(self):
        """Fetches and displays contact details (Including Address & Gender)."""
        query = """
        SELECT c.first_name, c.last_name, c.email, c.phone_number, c.gender,
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
            self.ui.street_line.setText(contact.get("street", ""))
            self.ui.city_line.setText(contact.get("city", ""))
            self.ui.state_line.setText(contact.get("state", ""))
            self.ui.zip_line.setText(contact.get("zip_code", ""))
            self.ui.country_line.setText(contact.get("country", ""))
            self.ui.company_line.setText(contact.get("company_name", ""))
