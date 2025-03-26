from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QCheckBox, QHeaderView, QLineEdit, QMessageBox, QApplication, QMenu
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QAction

from models.models_contacts_create import ContactsCreate
from models.models_contacts_view import ContactsView
from models.models_contacts_update import ContactsUpdate
from views.py.ui_contacts_landing import Ui_contacts_landing
from datas.db_connection import DB_Connection

class ContactsLanding(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts_landing()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()

        # ✅ Enable mouse tracking for hover detection, mail button clicks
        self.ui.contacts_tbl.viewport().setMouseTracking(True)
        self.ui.contacts_tbl.viewport().installEventFilter(self)

        # ✅ Properly expand columns
        self.ui.contacts_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # ✅ Connect add_btn to add_contact function
        self.ui.add_btn.clicked.connect(self.add_contact)
        self.ui.search_line.textChanged.connect(self.search_contacts)  # Live search
        self.ui.delete_btn.clicked.connect(self.delete_contact)
        self.ui.sort_combo.currentIndexChanged.connect(self.sort_contacts)
        self.load_contacts(order_by="created_at", ascending=False)  # Default: Recently Added

        # ✅ Track currently highlighted row
        self.current_hover_row = -1

        # ✅ Hide label initially
        self.ui.selecteditems_lbl.hide()

        # ✅ Table headings settings
        self.ui.contacts_tbl.horizontalHeader().setStyleSheet("font-weight: 800;")

        # ✅ Search Icon
        search_icon = QIcon(":/Resources/search.svg")
        self.ui.search_line.addAction(search_icon, QLineEdit.LeadingPosition)

    def sort_contacts(self):
        """Sorts contacts based on the selected option from sort_combo."""
        selected_option = self.ui.sort_combo.currentText()

        if selected_option == "Alphabetical":
            self.load_contacts(order_by="name", ascending=True)
        elif selected_option == "Recently Added":
            self.load_contacts(order_by="created_at", ascending=False)
        elif selected_option == "Oldest":
            self.load_contacts(order_by="created_at", ascending=True)
        else:
            print("⚠️ Invalid sort option selected.")

    def add_contact(self):
        """Opens the Contacts Create form inside the MDI subwindow."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        MDIManager.load_into_mdi(ContactsCreate)

    def view_contact(self, row):
        """Loads the View Contact form inside the MDI area."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        contact_id_item = self.ui.contacts_tbl.item(row, 0)  # ✅ Get Contact ID
        if not contact_id_item:
            print("❌ No contact ID found for this row.")
            return

        contact_id = contact_id_item.text().strip()
        MDIManager.load_into_mdi(lambda: ContactsView(contact_id))  # ✅ Load into MDI

    def edit_contact(self, row):
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        """Loads the Edit Contact form inside the MDI area."""
        contact_id_item = self.ui.contacts_tbl.item(row, 0)  # ✅ Get Contact ID
        if not contact_id_item:
            print("❌ No contact ID found for this row.")
            return

        contact_id = contact_id_item.text().strip()
        MDIManager.load_into_mdi(lambda: ContactsUpdate(contact_id))

    def delete_contact(self):
        """Deletes selected contacts after confirmation."""
        selected_ids = []

        for row in range(self.ui.contacts_tbl.rowCount()):
            cell_widget = self.ui.contacts_tbl.cellWidget(row, 1)  # ✅ Checkbox is in column 1
            if cell_widget:
                checkbox = cell_widget.layout().itemAt(0).widget()
                if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                    # ✅ Get contact_id from hidden column 0
                    contact_id_item = self.ui.contacts_tbl.item(row, 0)
                    if contact_id_item:
                        selected_ids.append(contact_id_item.text().strip())

        if not selected_ids:
            QMessageBox.information(self, "No Selection", "Please select at least one contact to delete.")
            return

        # ✅ Show confirmation dialog
        confirmation = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(selected_ids)} selected contact(s)?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirmation == QMessageBox.Yes:
            # ✅ Execute delete query
            query = f"DELETE FROM contact WHERE contact_id IN ({','.join(['%s'] * len(selected_ids))})"
            success = self.db_conn.execute_query(query, tuple(selected_ids))

            if success:
                self.load_contacts()  # ✅ Refresh table
                QMessageBox.information(self, "Deleted", f"Successfully deleted {len(selected_ids)} contact(s).")
            else:
                QMessageBox.critical(self, "Error", "Failed to delete selected contacts.")

    def load_contacts(self, order_by="created_at", ascending=False):
        """Fetches contacts from the database and populates the QTableWidget."""
        order_direction = "ASC" if ascending else "DESC"

        query = f"""
            SELECT
                c.contact_id,
                CONCAT_WS(' ', c.first_name, c.last_name) AS name,
                c.email,
                c.phone_number,
                COALESCE(comp.company_name, '') AS company_name,
                c.created_at
            FROM contact c
            LEFT JOIN company comp ON c.company_id = comp.company_id
            ORDER BY {order_by} {order_direction}
        """

        contacts = self.db_conn.fetch_all(query)
        if contacts is None:
            print("❌ Failed to fetch contacts.")
            return

        headers = ["ID (Hidden)", "Name", "Email", "Phone", "Company"]
        self.ui.contacts_tbl.setColumnCount(len(headers))
        self.ui.contacts_tbl.setHorizontalHeaderLabels(headers)
        self.ui.contacts_tbl.setRowCount(len(contacts))

        for row_idx, contact in enumerate(contacts):
            contact_id_item = QTableWidgetItem(str(contact["contact_id"]))
            contact_id_item.setFlags(Qt.ItemIsEnabled)
            self.ui.contacts_tbl.setItem(row_idx, 0, contact_id_item)

            self.ui.contacts_tbl.setCellWidget(row_idx, 1, self.create_name_cell(contact["name"], row_idx))
            self.ui.contacts_tbl.setItem(row_idx, 2, QTableWidgetItem(contact["email"]))
            self.ui.contacts_tbl.setItem(row_idx, 3, QTableWidgetItem(contact["phone_number"]))
            self.ui.contacts_tbl.setItem(row_idx, 4, QTableWidgetItem(contact["company_name"]))

        self.ui.contacts_tbl.setColumnHidden(0, True)
        print(f"✅ Contacts loaded successfully! Sorted by {order_by} ({'ASC' if ascending else 'DESC'})")

    def search_contacts(self):
        """Search contacts by name, email, phone, or company."""
        search_term = self.ui.search_line.text().strip()
        if not search_term:
            self.load_contacts()
            return

        query = """
            SELECT
                c.contact_id,
                CONCAT_WS(' ', c.first_name, c.last_name) AS name,
                c.email,
                c.phone_number,
                COALESCE(comp.company_name, '') AS company_name
            FROM contact c
            LEFT JOIN company comp ON c.company_id = comp.company_id
            WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR c.email LIKE %s
                  OR c.phone_number LIKE %s OR comp.company_name LIKE %s
        """

        params = (f"%{search_term}%",) * 5
        results = self.db_conn.fetch_all(query, params)

        if results is None:
            print("❌ Error fetching search results.")
            return

        self.ui.contacts_tbl.setRowCount(len(results))
        for row_idx, contact in enumerate(results):
            contact_id_item = QTableWidgetItem(str(contact["contact_id"]))
            contact_id_item.setFlags(contact_id_item.flags() & ~Qt.ItemIsEditable)
            self.ui.contacts_tbl.setItem(row_idx, 0, contact_id_item)

            self.ui.contacts_tbl.setCellWidget(row_idx, 1, self.create_name_cell(contact["name"], row_idx))
            self.ui.contacts_tbl.setItem(row_idx, 2, QTableWidgetItem(contact["email"]))
            self.ui.contacts_tbl.setItem(row_idx, 3, QTableWidgetItem(contact["phone_number"]))
            self.ui.contacts_tbl.setItem(row_idx, 4, QTableWidgetItem(contact["company_name"]))

        print(f"✅ {len(results)} contacts found for '{search_term}'.")


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
            self.ui.contacts_tbl.cellWidget(row, 1) and
            self.ui.contacts_tbl.cellWidget(row, 1).layout() and
            self.ui.contacts_tbl.cellWidget(row, 1).layout().itemAt(0) and
            self.ui.contacts_tbl.cellWidget(row, 1).layout().itemAt(0).widget().isChecked()
            for row in range(self.ui.contacts_tbl.rowCount())
            if self.ui.contacts_tbl.cellWidget(row, 1)  # ✅ Ensure it's not None
        )

        print(f"🔍 Selected Count: {selected_count}")  # ✅ Debugging

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

    def hide_all_icons(self):
        """Removes all icons from the Company column."""
        for row in range(self.ui.contacts_tbl.rowCount()):
            self.ui.contacts_tbl.removeCellWidget(row, 4)


    def show_icons(self, row):
        """Displays icons in the 'Company' column when hovered over a row."""
        table = self.ui.contacts_tbl
        if row < 0:
            return

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignRight)

        # ✅ Mail button
        mail_button = self.create_icon_button(":/Resources/mail.svg", "Message")
        mail_button.clicked.connect(lambda: self.mail(row))

        # ✅ Menu button (Options for View/Edit)
        menu_button = self.create_icon_button(":/Resources/menu.svg", "Options")
        menu_button.clicked.connect(lambda _, btn=menu_button: self.show_contact_menu(row, btn))

        layout.addWidget(mail_button)
        layout.addWidget(menu_button)
        widget.setLayout(layout)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        table.setCellWidget(row, 4, widget)  # ✅ Last column (Company)

    def mail(self, row):
        """Opens the email dialog positioned at the bottom-right of MainWindow."""
        from models.models_contacts_email import ContactsEmail
        from models.models_authentication import MainWindow  # Ensure we get MainWindow

        # ✅ Get the contact's email
        email_item = self.ui.contacts_tbl.item(row, 2)  # Column index for email
        if not email_item:
            print("❌ No email found for this contact.")
            return

        contact_email_address = email_item.text().strip()

        # ✅ Get the MainWindow instance
        main_window = next(
            (w for w in QApplication.instance().topLevelWidgets() if isinstance(w, MainWindow)), None
        )
        if not main_window:
            print("❌ MainWindow not found.")
            return

        # ✅ Create and position the dialog
        self.email_dialog = ContactsEmail(contact_email_address, parent=main_window)
        self.email_dialog.move_to_bottom_right()
        self.email_dialog.show()

    def show_contact_menu(self, row, button):
        """Displays a menu with 'View' and 'Edit' options for a contact."""
        menu = QMenu(self)

        # ✅ View Contact Action
        view_action = QAction("View Contact Details", self)
        view_action.triggered.connect(lambda: self.view_contact(row))

        # ✅ Edit Contact Action
        edit_action = QAction("Edit Contact", self)
        edit_action.triggered.connect(lambda: self.edit_contact(row))

        # ✅ Apply hover effects
        menu.setStyleSheet("""
            QMenu { background-color: white; border: 1px solid #ccc; }
            QMenu::item { padding: 8px 20px; }
            QMenu::item:selected { background-color: #f0f0f0; }
        """)

        menu.addAction(view_action)
        menu.addAction(edit_action)

        # ✅ Get cursor position and show menu
        cursor_pos = button.mapToGlobal(button.rect().bottomLeft())
        menu.exec(cursor_pos)
