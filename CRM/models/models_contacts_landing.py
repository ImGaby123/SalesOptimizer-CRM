from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from models.models_contacts_create import ContactsCreate
from views.py.ui_contacts_landing import Ui_contacts_landing
from datas.db_connection import Database

class ContactsLanding(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts_landing()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = Database()

        # ✅ Connect add_btn to add_contact function
        self.ui.add_btn.clicked.connect(self.add_contact)
        self.load_contacts()
        self.ui.search_line.textChanged.connect(self.search_contacts)  # Live search

    def add_contact(self):
        """Opens the Contacts Create form inside the MDI subwindow."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        MDIManager.load_into_mdi(ContactsCreate)  # ✅ Now just one line

    def load_contacts(self):
        """Fetches contacts from the database and populates the QTableWidget with required fields."""
        query = """
            SELECT
                c.contact_id, c.first_name, c.middle_name, c.last_name,
                c.email, c.phone_number, COALESCE(comp.company_name, '') AS company_name
            FROM contact c
            LEFT JOIN owner o ON c.contact_id = o.contact_owner_id
            LEFT JOIN company comp ON o.company_id = comp.company_id
        """

        # Execute query and fetch all results
        contacts = self.db_conn.fetch_all(query)

        if contacts is None:
            print("❌ Failed to fetch contacts.")
            return

        # Define column headers
        headers = ["ID (Hidden)", "First Name", "Middle Name", "Last Name", "Email", "Phone Number", "Company", "Actions"]

        # Clear previous data and set up table structure
        self.ui.contacts_tbl.clear()
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setRowCount(len(contacts))

        # Populate table with data
        for row_idx, contact in enumerate(contacts):
            for col_idx, value in enumerate(contact.values()):
                item = QTableWidgetItem(str(value) if value is not None else "")

                # Hide contact_id (First Column)
                if col_idx == 0:
                    item.setFlags(item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable)
                    self.ui.contacts_tbl.setColumnHidden(0, True)

                self.ui.contacts_tbl.setItem(row_idx, col_idx, item)

            # Add action buttons
            self.add_icons(row_idx)

        print("✅ Contacts loaded successfully!")

    def search_contacts(self):
        """Search for contacts by first name, last name, or company name and update the table."""
        search_term = self.ui.search_line.text().strip()

        # If search is empty, reload all contacts
        if not search_term:
            self.load_contacts()
            return

        query = """
            SELECT
                c.contact_id, c.first_name, c.middle_name, c.last_name,
                c.email, c.phone_number, COALESCE(comp.company_name, '') AS company_name
            FROM contact c
            LEFT JOIN owner o ON c.contact_id = o.contact_owner_id
            LEFT JOIN company comp ON o.company_id = comp.company_id
            WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR comp.company_name LIKE %s
        """

        params = (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")
        results = self.db_conn.fetch_all(query, params)

        if results is None:
            print("❌ Error fetching search results.")
            return

        print(f"🔍 Query Results: {results}")  # Debugging

        # Define headers
        headers = ["ID (Hidden)", "First Name", "Middle Name", "Last Name", "Email", "Phone Number", "Company", "Actions"]

        # Reset table
        self.ui.contacts_tbl.clear()
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setRowCount(len(results))

        for row_idx, contact in enumerate(results):
            for col_idx, value in enumerate(contact.values()):
                item = QTableWidgetItem(str(value) if value is not None else "")

                # Hide contact_id (First Column)
                if col_idx == 0:
                    item.setFlags(Qt.ItemIsEnabled)  # Make uneditable but selectable
                    self.ui.contacts_tbl.setColumnHidden(0, True)

                self.ui.contacts_tbl.setItem(row_idx, col_idx, item)

            # Add action buttons
            self.add_icons(row_idx)

        print(f"✅ {len(results)} contacts found for '{search_term}'.")

    def add_icons(self, row):
        """Adds action buttons (Mail and Menu) to the last column."""
        table = self.ui.contacts_tbl
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)  # Adjust spacing between buttons

        # Create an invisible spacer to push buttons to the right
        spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Base button style (borderless, transparent, hand cursor)
        base_style = """
            QPushButton {
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.1);
                border-radius: 5px;
            }
        """

        # Create mail button
        mail_button = QPushButton()
        mail_button.setIcon(QIcon(":/Resources/mail.svg"))
        mail_button.setFixedSize(25, 25)
        mail_button.setCursor(Qt.PointingHandCursor)
        mail_button.setStyleSheet(base_style)

        # Create menu button
        menu_button = QPushButton()
        menu_button.setIcon(QIcon(":/Resources/menu.svg"))
        menu_button.setFixedSize(25, 25)
        menu_button.setCursor(Qt.PointingHandCursor)
        menu_button.setStyleSheet(base_style)

        # Add spacer first, then buttons (this pushes them to the right)
        layout.addItem(spacer)
        layout.addWidget(mail_button)
        layout.addWidget(menu_button)

        widget.setLayout(layout)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # ✅ Use the last column index dynamically
        last_column = table.columnCount() - 1
        table.setCellWidget(row, last_column, widget)
