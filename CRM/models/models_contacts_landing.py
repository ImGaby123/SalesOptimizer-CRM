from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QSpacerItem, QCheckBox, QHeaderView, QLineEdit
)
from PySide6.QtCore import Qt, QEvent
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

        # ✅ Enable mouse tracking for hover detection
        self.ui.contacts_tbl.viewport().setMouseTracking(True)

        # ✅ Properly expand columns
        self.ui.contacts_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ✅ Connect add_btn to add_contact function
        self.ui.add_btn.clicked.connect(self.add_contact)
        self.load_contacts()
        self.ui.search_line.textChanged.connect(self.search_contacts)  # Live search

        # ✅ Add hover event filter
        self.ui.contacts_tbl.viewport().installEventFilter(self)

        # ✅ Track currently highlighted row
        self.current_hover_row = -1

        # ✅ Hide label initially
        self.ui.selecteditems_lbl.hide()

        # ✅ Table headings settings
        self.ui.contacts_tbl.horizontalHeader().setStyleSheet("font-weight: 800;")

        # ✅ Search Icon
        search_icon = QIcon(":/Resources/search.svg")
        self.ui.search_line.addAction(search_icon, QLineEdit.LeadingPosition)

    def add_contact(self):
        """Opens the Contacts Create form inside the MDI subwindow."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        MDIManager.load_into_mdi(ContactsCreate)

    def load_contacts(self):
        """Fetches contacts from the database and populates the QTableWidget."""
        query = """
            SELECT
                c.contact_id,
                CONCAT_WS(' ', c.first_name, c.middle_name, c.last_name) AS name,
                c.email,
                c.phone_number,
                COALESCE(comp.company_name, '') AS company_name
            FROM contact c
            LEFT JOIN owner o ON c.contact_id = o.contact_owner_id
            LEFT JOIN company comp ON o.company_id = comp.company_id
        """

        contacts = self.db_conn.fetch_all(query)
        if contacts is None:
            print("❌ Failed to fetch contacts.")
            return

        # ✅ Define column headers
        headers = ["Name", "Email", "Phone Number", "Company"]
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setRowCount(len(contacts))

        # ✅ Populate table
        for row_idx, contact in enumerate(contacts):
            self.ui.contacts_tbl.setCellWidget(row_idx, 0, self.create_name_cell(contact["name"], row_idx))
            self.ui.contacts_tbl.setItem(row_idx, 1, QTableWidgetItem(contact["email"]))
            self.ui.contacts_tbl.setItem(row_idx, 2, QTableWidgetItem(contact["phone_number"]))
            self.ui.contacts_tbl.setItem(row_idx, 3, QTableWidgetItem(contact["company_name"]))

        print("✅ Contacts loaded successfully!")

    def create_name_cell(self, name, row):
        """Creates a widget with a checkbox and properly spaced name."""
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(5, 0, 0, 0)
        layout.setSpacing(12)  # ✅ Adjusted for perfect monospace spacing

        checkbox = QCheckBox()
        checkbox.stateChanged.connect(lambda: self.update_selected_count())

        name_label = QLabel(name)

        layout.addWidget(checkbox)
        layout.addWidget(name_label)
        layout.addStretch()  # ✅ Push elements to the left for alignment
        widget.setLayout(layout)

        return widget

    def update_selected_count(self):
        """Updates the count of selected items and toggles label visibility."""
        selected_count = sum(
            self.ui.contacts_tbl.cellWidget(row, 0).layout().itemAt(0).widget().isChecked()
            for row in range(self.ui.contacts_tbl.rowCount())
        )

        if selected_count > 0:
            self.ui.selecteditems_lbl.setText(f"Selected {selected_count} Item{'s' if selected_count > 1 else ''}")
            self.ui.selecteditems_lbl.show()
        else:
            self.ui.selecteditems_lbl.hide()

    def search_contacts(self):
        """Search for contacts by name, email, phone, or company name and update the table."""
        search_term = self.ui.search_line.text().strip()

        if not search_term:
            self.load_contacts()
            return

        query = """
            SELECT
                c.contact_id,
                CONCAT_WS(' ', c.first_name, c.middle_name, c.last_name) AS name,
                c.email,
                c.phone_number,
                COALESCE(comp.company_name, '') AS company_name
            FROM contact c
            LEFT JOIN owner o ON c.contact_id = o.contact_owner_id
            LEFT JOIN company comp ON o.company_id = comp.company_id
            WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR c.email LIKE %s OR c.phone_number LIKE %s OR comp.company_name LIKE %s
        """

        params = (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")
        results = self.db_conn.fetch_all(query, params)

        if results is None:
            print("❌ Error fetching search results.")
            return

        print(f"🔍 Query Results: {results}")

        # ✅ Reset headers before populating search results
        headers = ["Name", "Email", "Phone Number", "Company"]
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setRowCount(len(results))

        for row_idx, contact in enumerate(results):
            self.ui.contacts_tbl.setCellWidget(row_idx, 0, self.create_name_cell(contact["name"], row_idx))
            self.ui.contacts_tbl.setItem(row_idx, 1, QTableWidgetItem(contact["email"]))
            self.ui.contacts_tbl.setItem(row_idx, 2, QTableWidgetItem(contact["phone_number"]))
            self.ui.contacts_tbl.setItem(row_idx, 3, QTableWidgetItem(contact["company_name"]))

        print(f"✅ {len(results)} contacts found for '{search_term}'.")

    def eventFilter(self, obj, event):
        """Handles row hover events to show/hide icons dynamically."""
        if obj == self.ui.contacts_tbl.viewport():
            if event.type() == QEvent.MouseMove:
                row = self.ui.contacts_tbl.rowAt(event.pos().y())

                if row >= 0 and row != self.current_hover_row:
                    self.hide_all_icons()
                    self.show_icons(row)
                    self.current_hover_row = row

            elif event.type() == QEvent.Leave:
                self.hide_all_icons()
                self.current_hover_row = -1

        return super().eventFilter(obj, event)

    def create_icon_button(self, icon_path, tooltip):
        """Creates a styled QPushButton with an icon and tooltip."""
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setFixedSize(25, 25)
        button.setCursor(Qt.PointingHandCursor)
        button.setToolTip(tooltip)
        button.setStyleSheet("""
            QPushButton {
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                background-color: rgba(100, 100, 100, 0.2);
                border-radius: 5px;
            }
        """)
        return button  # ✅ Now correctly placed

    def show_icons(self, row):
        """Displays icons in the 'Company' column when hovered over a row."""
        table = self.ui.contacts_tbl
        if row < 0:
            return

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignRight)

        # ✅ Create buttons using the correctly defined method
        mail_button = self.create_icon_button(":/Resources/mail.svg", "Message")
        menu_button = self.create_icon_button(":/Resources/menu.svg", "More")

        # ✅ Add buttons to layout
        layout.addWidget(mail_button)
        layout.addWidget(menu_button)

        widget.setLayout(layout)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        table.setCellWidget(row, 3, widget)  # ✅ Company column is **index 3**

    def hide_all_icons(self):
        """Removes all icons from the Company column."""
        for row in range(self.ui.contacts_tbl.rowCount()):
            self.ui.contacts_tbl.removeCellWidget(row, 3)
