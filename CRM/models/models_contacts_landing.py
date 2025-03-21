from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem, QCheckBox
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

        # ✅ Connect add_btn to add_contact function
        self.ui.add_btn.clicked.connect(self.add_contact)
        self.load_contacts()
        self.ui.search_line.textChanged.connect(self.search_contacts)  # Live search

        # ✅ Add hover event filter
        self.ui.contacts_tbl.viewport().installEventFilter(self)

        # Track currently highlighted row to remove icons when mouse moves
        self.current_hover_row = -1

        # ✅ Initially hide selected items label
        self.ui.selecteditems_lbl.hide()

    def add_contact(self):
        """Opens the Contacts Create form inside the MDI subwindow."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        MDIManager.load_into_mdi(ContactsCreate)

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

        # ✅ Define column headers (No "Select" header for better alignment)
        headers = ["ID (Hidden)", "First Name", "Middle Name", "Last Name", "Email", "Phone Number", "Company"]

        # ✅ Reset table
        self.ui.contacts_tbl.clear()
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setRowCount(len(contacts))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setColumnHidden(0, True)  # Hide contact_id column

        for row_idx, contact in enumerate(contacts):
            contact_values = [
                contact["contact_id"], contact["first_name"], contact["middle_name"],
                contact["last_name"], contact["email"], contact["phone_number"], contact["company_name"]
            ]

            # ✅ Create checkbox widget inside "First Name" column
            checkbox_widget = QWidget()
            layout = QHBoxLayout(checkbox_widget)
            layout.setContentsMargins(0, 0, 0, 0)  # ✅ Ensure tight alignment
            layout.setSpacing(8)  # ✅ Reduce space between checkbox and text

            checkbox = QCheckBox()
            checkbox.setFixedSize(15, 15)  # ✅ Standardized size
            checkbox.stateChanged.connect(self.update_selected_count)

            name_label = QLabel(contact_values[1])  # First Name text
            name_label.setStyleSheet("font-family: monospace; padding-left: 5px;")  # ✅ Monospace for consistency

            layout.addWidget(checkbox)
            layout.addWidget(name_label)
            layout.addStretch()  # ✅ Push elements to the left for even spacing
            checkbox_widget.setLayout(layout)

            # ✅ Insert the checkbox + name inside "First Name" column (Index 1)
            self.ui.contacts_tbl.setCellWidget(row_idx, 1, checkbox_widget)

            # ✅ Set other columns with correct data
            for col_idx in range(2, len(contact_values)):  # Skipping contact_id (Hidden)
                item = QTableWidgetItem(str(contact_values[col_idx]) if contact_values[col_idx] else "")
                self.ui.contacts_tbl.setItem(row_idx, col_idx, item)

        print("✅ Contacts loaded successfully!")

    def update_selected_count(self):
        """Updates the selected items label based on checked checkboxes."""
        selected_count = sum(
            1 for row in range(self.ui.contacts_tbl.rowCount()) if self.ui.contacts_tbl.cellWidget(row, 1).layout().itemAt(0).widget().isChecked()
        )

        if selected_count > 0:
            self.ui.selecteditems_lbl.setText(f"Selected {selected_count} Item{'s' if selected_count > 1 else ''}")
            self.ui.selecteditems_lbl.show()
        else:
            self.ui.selecteditems_lbl.hide()

    def eventFilter(self, obj, event):
        """Handles row hover events to show/hide icons dynamically."""
        if obj == self.ui.contacts_tbl.viewport():
            if event.type() == QEvent.MouseMove:
                row = self.ui.contacts_tbl.rowAt(event.pos().y())

                if row != self.current_hover_row:  # Only update when row changes
                    self.hide_all_icons()
                    self.show_icons(row)
                    self.current_hover_row = row

            elif event.type() == QEvent.Leave:
                self.hide_all_icons()
                self.current_hover_row = -1  # Reset tracking

        return super().eventFilter(obj, event)

    def show_icons(self, row):
        """Displays icons in the 'Company' column when hovered over a row."""
        table = self.ui.contacts_tbl
        if row < 0:
            return  # Skip invalid rows

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)  # Monospace spacing between icons
        layout.setAlignment(Qt.AlignRight)  # Align icons to the right

        # Spacer to push icons to the right
        spacer = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)

        # Create Mail button
        mail_button = QPushButton()
        mail_button.setIcon(QIcon(":/Resources/mail.svg"))
        mail_button.setFixedSize(25, 25)
        mail_button.setCursor(Qt.PointingHandCursor)
        mail_button.setStyleSheet("border: none; background: transparent;")

        # Create Menu button
        menu_button = QPushButton()
        menu_button.setIcon(QIcon(":/Resources/menu.svg"))
        menu_button.setFixedSize(25, 25)
        menu_button.setCursor(Qt.PointingHandCursor)
        menu_button.setStyleSheet("border: none; background: transparent;")

        layout.addWidget(mail_button)
        layout.addWidget(menu_button)

        widget.setLayout(layout)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        company_column = 6  # Company column index (Fixed icon placement issue)
        table.setCellWidget(row, company_column, widget)

    def hide_all_icons(self):
        """Removes all icons from the Company column to restore original text."""
        table = self.ui.contacts_tbl
        company_column = 6  # Company column index

        for row in range(table.rowCount()):
            if table.cellWidget(row, company_column):  # Only remove if icons exist
                table.removeCellWidget(row, company_column)

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

        # ✅ Define headers
        headers = ["ID (Hidden)", "First Name", "Middle Name", "Last Name", "Email", "Phone Number", "Company"]

        # ✅ Reset table
        self.ui.contacts_tbl.clear()
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setRowCount(len(results))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setColumnHidden(0, True)  # Hide contact_id column

        for row_idx, contact in enumerate(results):
            contact_values = [
                contact["contact_id"], contact["first_name"], contact["middle_name"],
                contact["last_name"], contact["email"], contact["phone_number"], contact["company_name"]
            ]

            # ✅ Create checkbox widget inside "First Name" column (Index 1)
            checkbox_widget = QWidget()
            layout = QHBoxLayout(checkbox_widget)
            layout.setContentsMargins(5, 0, 0, 0)
            layout.setSpacing(5)

            checkbox = QCheckBox()
            checkbox.stateChanged.connect(self.update_selected_count)

            name_label = QLabel(contact_values[1])  # First Name text
            layout.addWidget(checkbox)
            layout.addWidget(name_label)
            checkbox_widget.setLayout(layout)

            # ✅ Set checkbox + name inside "First Name" column (Index 1)
            self.ui.contacts_tbl.setCellWidget(row_idx, 1, checkbox_widget)

            # ✅ Set other columns with correct data
            for col_idx in range(2, len(contact_values)):  # Skipping contact_id (Hidden)
                item = QTableWidgetItem(str(contact_values[col_idx]) if contact_values[col_idx] else "")
                self.ui.contacts_tbl.setItem(row_idx, col_idx, item)

        print(f"✅ {len(results)} contacts found for '{search_term}'.")
