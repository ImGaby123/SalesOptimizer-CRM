from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QCheckBox, QHeaderView, QLineEdit, QMessageBox, QMenu
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QAction
from models.models_contacts_view import ContactsView
from views.py.ui_leads_landing import Ui_leads_landing
from datas.db_connection import DB_Connection

class LeadsLanding(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leads_landing()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()

        # ✅ Enable mouse tracking for hover detection, mail button clicks
        self.ui.leads_tbl.viewport().setMouseTracking(True)
        self.ui.leads_tbl.viewport().installEventFilter(self)

        # ✅ Properly expand columns
        self.ui.leads_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.search_line.textChanged.connect(self.search_leads)  # Live search
        self.ui.delete_btn.clicked.connect(self.delete_lead)
        self.ui.sort_combo.currentIndexChanged.connect(self.sort_leads)
        self.load_leads(order_by="created_at", ascending=False)  # Default: Recently Added

        # ✅ Track currently highlighted row
        self.current_hover_row = -1

        # ✅ Hide label initially
        self.ui.selecteditems_lbl.hide()

        # ✅ Table headings settings
        self.ui.leads_tbl.horizontalHeader().setStyleSheet("font-weight: 800;")

        # ✅ Search Icon
        search_icon = QIcon(":/Resources/search_white.svg")
        self.ui.search_line.addAction(search_icon, QLineEdit.LeadingPosition)

    def sort_leads(self):
        """Sorts leads based on the selected option from sort_combo."""
        selected_option = self.ui.sort_combo.currentText()

        if selected_option == "Alphabetical":
            # Sort by the 'name' alias (which is CONCAT_WS of first and last name)
            self.load_leads(order_by="name", ascending=True)
        elif selected_option == "Recently Added":
            # Sort by created_at without table alias here
            self.load_leads(order_by="created_at", ascending=False)
        elif selected_option == "Oldest":
            # Sort by created_at without table alias here
            self.load_leads(order_by="created_at", ascending=True)
        else:
            print("⚠️ Invalid sort option selected.")

    def view_lead(self, row):
        """Loads the View Contact form inside the MDI area."""
        from models.models_authentication import MDIManager  # ✅ Lazy import to avoid circular import
        lead_id_item = self.ui.leads_tbl.item(row, 0)  # ✅ Get Lead ID
        if not lead_id_item:
            print("❌ No lead ID found for this row.")
            return

        lead_id = lead_id_item.text().strip()

        # Query to get the contact_id associated with the lead_id
        query = "SELECT contact_id FROM leads WHERE lead_id = %s"
        contact_data = self.db_conn.fetch_one(query, (lead_id,))

        if not contact_data:
            print("❌ No contact found for this lead.")
            return

        contact_id = contact_data["contact_id"]

        # Load ContactsView with the contact_id
        MDIManager.load_into_mdi(lambda: ContactsView(contact_id))  # ✅ Load into MDI

    def delete_lead(self):
        """Deletes selected leads after confirmation."""
        selected_ids = []

        for row in range(self.ui.leads_tbl.rowCount()):
            cell_widget = self.ui.leads_tbl.cellWidget(row, 1)  # ✅ Checkbox is in column 1
            if cell_widget:
                checkbox = cell_widget.layout().itemAt(0).widget()
                if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                    # ✅ Get lead_id from hidden column 0
                    lead_id_item = self.ui.leads_tbl.item(row, 0)
                    if lead_id_item:
                        selected_ids.append(lead_id_item.text().strip())

        if not selected_ids:
            QMessageBox.information(self, "No Selection", "Please select at least one lead to delete.")
            return

        # ✅ Show confirmation dialog
        confirmation = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete {len(selected_ids)} selected lead(s)?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirmation == QMessageBox.Yes:
            # ✅ Execute delete query
            query = f"DELETE FROM leads WHERE lead_id IN ({','.join(['%s'] * len(selected_ids))})"
            success = self.db_conn.execute_query(query, tuple(selected_ids))

            if success:
                self.load_leads()  # ✅ Refresh table
                QMessageBox.information(self, "Deleted", f"Successfully deleted {len(selected_ids)} lead(s).")
            else:
                QMessageBox.critical(self, "Error", "Failed to delete selected leads.")

    def load_leads(self, order_by="created_at", ascending=False):
        """Fetches leads from the database and populates the QTableWidget."""
        order_direction = "ASC" if ascending else "DESC"

        # Add table alias `l.` if the column is `created_at`
        if order_by == "created_at":
            order_by = f"l.{order_by}"

        # Updated query to include lead_score
        query = f"""
            SELECT
                l.lead_id,
                CONCAT_WS(' ', c.first_name, c.last_name) AS name,
                COALESCE(comp.company_name, '') AS company_name,
                l.lead_score  -- Include lead_score in the query
            FROM leads l
            LEFT JOIN contact c ON l.contact_id = c.contact_id
            LEFT JOIN company comp ON c.company_id = comp.company_id
            ORDER BY {order_by} {order_direction}
        """

        leads = self.db_conn.fetch_all(query)
        if leads is None:
            print("❌ Failed to fetch leads.")
            return

        # Define headers to include 'Lead Score'
        headers = ["Lead ID (Hidden)", "Name", "Company Name", "Engagement Score", "Lead Score"]
        self.ui.leads_tbl.setColumnCount(len(headers))
        self.ui.leads_tbl.setHorizontalHeaderLabels(headers)
        self.ui.leads_tbl.setRowCount(len(leads))

        # Populate the table with the data
        for row_idx, lead in enumerate(leads):
            lead_id_item = QTableWidgetItem(str(lead["lead_id"]))
            lead_id_item.setFlags(Qt.ItemIsEnabled)  # Disable editing for Lead ID
            self.ui.leads_tbl.setItem(row_idx, 0, lead_id_item)

            self.ui.leads_tbl.setCellWidget(row_idx, 1, self.create_name_cell(lead["name"], row_idx))
            self.ui.leads_tbl.setItem(row_idx, 2, QTableWidgetItem(lead["company_name"]))

            # Add Lead Score to the last column
            self.ui.leads_tbl.setItem(row_idx, 4, QTableWidgetItem(str(lead["lead_score"])))

        self.ui.leads_tbl.setColumnHidden(0, True)  # Hide the Lead ID column
        print(f"✅ Leads loaded successfully! Sorted by {order_by} ({'ASC' if ascending else 'DESC'})")

    def search_leads(self):
        """Search leads by name, email, phone, or company."""
        search_term = self.ui.search_line.text().strip()
        if not search_term:
            self.load_leads()
            return

        query = """
            SELECT
                l.lead_id,
                CONCAT_WS(' ', c.first_name, c.last_name) AS name,
                c.email,
                c.phone_number,
                COALESCE(comp.company_name, '') AS company_name
            FROM leads l
            LEFT JOIN contact c ON l.contact_id = c.contact_id
            LEFT JOIN company comp ON c.company_id = comp.company_id
            WHERE c.first_name LIKE %s OR c.last_name LIKE %s OR c.email LIKE %s
                  OR c.phone_number LIKE %s OR comp.company_name LIKE %s
        """

        params = (f"%{search_term}%",) * 5
        results = self.db_conn.fetch_all(query, params)

        if results is None:
            print("❌ Error fetching search results.")
            return

        self.ui.leads_tbl.setRowCount(len(results))
        for row_idx, lead in enumerate(results):
            lead_id_item = QTableWidgetItem(str(lead["lead_id"]))
            lead_id_item.setFlags(lead_id_item.flags() & ~Qt.ItemIsEditable)
            self.ui.leads_tbl.setItem(row_idx, 0, lead_id_item)

            self.ui.leads_tbl.setCellWidget(row_idx, 1, self.create_name_cell(lead["name"], row_idx))
            self.ui.leads_tbl.setItem(row_idx, 2, QTableWidgetItem(lead["email"]))
            self.ui.leads_tbl.setItem(row_idx, 3, QTableWidgetItem(lead["phone_number"]))
            self.ui.leads_tbl.setItem(row_idx, 4, QTableWidgetItem(lead["company_name"]))

        print(f"✅ {len(results)} leads found for '{search_term}'.")

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
            self.ui.leads_tbl.cellWidget(row, 1) and
            self.ui.leads_tbl.cellWidget(row, 1).layout() and
            self.ui.leads_tbl.cellWidget(row, 1).layout().itemAt(0) and
            self.ui.leads_tbl.cellWidget(row, 1).layout().itemAt(0).widget().isChecked()
            for row in range(self.ui.leads_tbl.rowCount())
            if self.ui.leads_tbl.cellWidget(row, 1)  # ✅ Ensure it's not None
        )

        print(f"🔍 Selected Count: {selected_count}")  # ✅ Debugging

        if selected_count > 0:
            self.ui.selecteditems_lbl.setText(f"Selected {selected_count} Item{'s' if selected_count > 1 else ''}")
            self.ui.selecteditems_lbl.show()
        else:
            self.ui.selecteditems_lbl.hide()

    def eventFilter(self, obj, event):
        """Handles row hover events to show/hide icons dynamically."""
        if obj == self.ui.leads_tbl.viewport():
            if event.type() == QEvent.MouseMove:
                row = self.ui.leads_tbl.rowAt(event.pos().y())

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
        """Removes all icons from the 'Company' column."""
        for row in range(self.ui.leads_tbl.rowCount()):
            self.ui.leads_tbl.removeCellWidget(row, 4)

    def show_icons(self, row):
        """Displays icons in the 'Company' column when hovered over a row."""
        table = self.ui.leads_tbl
        if row < 0:
            return

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignRight)

        # ✅ Menu button (Options for View/Edit)
        menu_button = self.create_icon_button(":/Resources/menu.svg", "Options")
        menu_button.clicked.connect(lambda _, btn=menu_button: self.show_lead_menu(row, btn))

        layout.addWidget(menu_button)
        widget.setLayout(layout)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        table.setCellWidget(row, 4, widget)  # ✅ Last column (Company)

    def show_lead_menu(self, row, button):
        """Displays a menu with 'View', 'Edit', and 'Add to Leads' options for a lead."""
        menu = QMenu(self)

        # ✅ Lead Profile Action
        lead_profile_action = QAction("Lead Profile", self)
        lead_profile_action.triggered.connect(lambda: self.view_lead_profile(row))

        # ✅ View Lead Action
        view_action = QAction("View Lead Details", self)
        view_action.triggered.connect(lambda: self.view_lead(row))

        # ✅ Apply hover effects
        menu.setStyleSheet("""
            QMenu { background-color: white; border: 1px solid #ccc; }
            QMenu::item { padding: 8px 20px; }
            QMenu::item:selected { background-color: #f0f0f0; }
        """)

        menu.addAction(lead_profile_action)
        menu.addAction(view_action)

        # ✅ Get cursor position and show menu
        cursor_pos = button.mapToGlobal(button.rect().bottomLeft())
        menu.exec(cursor_pos)

    ################################
    # View Lead Profile functions
    ################################
    def view_lead_profile(self, row):
        """Loads the lead's profile (detailed view) into the MDI area."""
        from models.models_authentication import MDIManager  # ✅ Lazy import
        from models.models_leads_profile import LeadsProfile  # ✅ Your target view

        lead_id_item = self.ui.leads_tbl.item(row, 0)
        if not lead_id_item:
            print("❌ No lead ID found for this row.")
            return

        lead_id = lead_id_item.text().strip()

        query = "SELECT contact_id FROM leads WHERE lead_id = %s"
        contact_data = self.db_conn.fetch_one(query, (lead_id,))

        if not contact_data:
            print("❌ No contact found for this lead.")
            return

        contact_id = contact_data["contact_id"]

        MDIManager.load_into_mdi(lambda: LeadsProfile(contact_id))

