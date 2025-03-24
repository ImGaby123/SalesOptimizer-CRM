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
