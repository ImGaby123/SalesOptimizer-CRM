from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from PySide6.QtCore import Qt
from views.py.ui_leads_profile import Ui_leads_profile
from datas.db_connection import DB_Connection


class LeadsProfile(QWidget):
    def __init__(self, contact_id):
        super().__init__()
        self.contact_id = contact_id
        self.ui = Ui_leads_profile()
        self.ui.setupUi(self)

        # Initialize database connection
        self.db_conn = DB_Connection()

        # Load contact info and opportunities table
        self.contact_info()
        self.opportunities_table()

        # Connect buttons to their handlers
        self.ui.add_btn.clicked.connect(self.add_opportunity)
        self.ui.edit_btn.clicked.connect(self.edit_opportunity)
        self.ui.delete_btn.clicked.connect(self.delete_opportunity)

        # Clickable Radiobuttons
        self.ui.qualification_radio.clicked.connect(lambda: self.set_opportunity_status("Qualification"))
        self.ui.negotiating_radio.clicked.connect(lambda: self.set_opportunity_status("Negotiating"))
        self.ui.approval_radio.clicked.connect(lambda: self.set_opportunity_status("Approval"))

        # View Full Contact Info
        self.ui.full_info_lbl.mousePressEvent = lambda event: self.view_contact_info()

        # Code for going back to leads_landing
        self.ui.back_btn.clicked.connect(self.go_back)

    def go_back(self):
        """Returns to the ContactsLanding form."""
        from models.models_authentication import MDIManager
        from models.models_leads_landing import LeadsLanding
        MDIManager.load_into_mdi(LeadsLanding)

    def view_contact_info(self):
        """Load full contact info in the MDI."""
        from models.models_authentication import MDIManager
        from models.models_contacts_view import ContactsView  # Adjust this import as needed

        if not self.contact_id:
            return

        MDIManager.load_into_mdi(lambda: ContactsView(self.contact_id))

    def contact_info(self):
        """Loads contact information into the respective labels."""
        query = """
            SELECT c.first_name, c.last_name, c.phone_number, c.job_title, c.email,
                   comp.company_name, ls.source_name
            FROM contact c
            JOIN company comp ON c.company_id = comp.company_id
            LEFT JOIN lead_source ls ON c.contact_id = ls.source_id
            WHERE c.contact_id = %s
        """
        contact_data = self.db_conn.fetch_one(query, (self.contact_id,))

        if contact_data:
            name = f"{contact_data['first_name']} {contact_data['last_name']}"
            self.ui.name_lbl.setText(name)
            self.ui.name_lbl_2.setText(name)
            self.ui.email_lbl.setText(contact_data['email'])
            self.ui.company_lbl.setText(contact_data['company_name'])
            self.ui.company_lbl_2.setText(contact_data['company_name'])
            self.ui.lead_source_value_lbl.setText(contact_data['source_name'] if contact_data['source_name'] else "N/A")

    def add_opportunity(self):
        """Open AddOpportunity dialog."""
        from models.models_add_opportunity import AddOpportunity
        dialog = AddOpportunity(self.contact_id, self)
        dialog.exec()

    def edit_opportunity(self):
        """Open EditOpportunity dialog for the selected opportunity."""
        selected_row = self.ui.opportunities_tbl.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an opportunity first!")
            return

        opportunity_id = self.ui.opportunities_tbl.item(selected_row, 0).text()

        from models.models_edit_opportunity import EditOpportunity
        dialog = EditOpportunity(self.contact_id, opportunity_id, self)
        dialog.exec()

    def delete_opportunity(self):
        """Deletes the selected opportunity from the database and resets opportunity details."""
        # Get selected row
        selected_row = self.ui.opportunities_tbl.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an opportunity first!")
            return

        # Get opportunity_id from the first column (hidden)
        opportunity_id_item = self.ui.opportunities_tbl.item(selected_row, 0)
        if not opportunity_id_item:
            QMessageBox.warning(self, "Error", "Unable to find the opportunity ID.")
            return

        opportunity_id = opportunity_id_item.text()

        # Confirm deletion with the user
        confirm = QMessageBox.question(
            self, "Confirm Deletion", f"Are you sure you want to delete opportunity {opportunity_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        # Execute deletion query
        delete_query = "DELETE FROM opportunity WHERE opportunity_id = %s"

        try:
            self.db_conn.execute_query(delete_query, (opportunity_id,))
            QMessageBox.information(self, "Success", "Opportunity deleted successfully.")

            # Refresh the table to reflect the changes
            self.opportunities_table()

            # Reset opportunity details labels to default state (clear or placeholder)
            self.reset_opportunity_details()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete opportunity:\n{e}")

    def reset_opportunity_details(self):
        """Resets the opportunity details to default/empty state."""
        self.ui.opportunity_title_lbl.setText("N/A")
        self.ui.opportunity_cost_lbl.setText("0.00")
        self.ui.opportunity_date_lbl.setText("N/A")
        self.ui.opportunity_details_lbl.setText("N/A")

    def opportunities_table(self):
        """Populates the opportunities table with opportunity titles linked to this contact."""
        self.ui.opportunities_tbl.setRowCount(0)  # Clear existing rows
        self.ui.opportunities_tbl.setColumnCount(2)
        self.ui.opportunities_tbl.setHorizontalHeaderLabels(["ID", "Opportunity Title"])
        self.ui.opportunities_tbl.setColumnHidden(0, True)  # Hide the ID column

        query = """
            SELECT opportunity_id, opportunity_title
            FROM opportunity
            WHERE contact_id = %s
            ORDER BY created_at DESC
        """
        results = self.db_conn.fetch_all(query, (self.contact_id,))

        for row_idx, row_data in enumerate(results):
            self.ui.opportunities_tbl.insertRow(row_idx)
            self.ui.opportunities_tbl.setItem(row_idx, 0, QTableWidgetItem(str(row_data["opportunity_id"])))
            self.ui.opportunities_tbl.setItem(row_idx, 1, QTableWidgetItem(row_data["opportunity_title"]))

        # Table Appearance
        table = self.ui.opportunities_tbl
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)

        # Connect click signal
        table.cellClicked.connect(self.load_opportunity_details)

    def load_opportunity_details(self, row, column):
        """Loads opportunity details into labels when a row is clicked."""
        opportunity_id_item = self.ui.opportunities_tbl.item(row, 0)
        if not opportunity_id_item:
            return

        opportunity_id = opportunity_id_item.text()

        query = """
            SELECT opportunity_title, opportunity_cost, date, opportunity_details
            FROM opportunity
            WHERE opportunity_id = %s
        """
        data = self.db_conn.fetch_one(query, (opportunity_id,))
        if data:
            self.ui.opportunity_title_lbl.setText(data["opportunity_title"] or "N/A")
            self.ui.opportunity_cost_lbl.setText(f"{data['opportunity_cost']:.2f}" if data["opportunity_cost"] else "0.00")
            self.ui.opportunity_date_lbl.setText(data["date"].strftime("%Y-%m-%d") if data["date"] else "N/A")
            self.ui.opportunity_details_lbl.setText(data["opportunity_details"] or "N/A")

        # NEW: Reflect the status for the selected opportunity
        self.opportunity_status_indicator(opportunity_id)

    def opportunity_status_indicator(self, opportunity_id):
        """Updates progress bar and radio buttons based on the selected opportunity's status."""
        query = "SELECT opportunity_status FROM opportunity WHERE opportunity_id = %s"
        data = self.db_conn.fetch_one(query, (opportunity_id,))

        if not data:
            return

        status = data["opportunity_status"]

        # Map status to progress bar value
        status_to_value = {
            "Prospecting": 11,
            "Qualification": 27,
            "Negotiating": 43,
            "Approval": 58,
            "Closed Loss": 77,
            "Closed Won": 100,
        }

        progress_value = status_to_value.get(status, 0)
        self.ui.opportunity_status_bar.setValue(progress_value)

        # Reset all radio buttons first
        self.ui.prospecting_radio.setChecked(False)
        self.ui.qualification_radio.setChecked(False)
        self.ui.negotiating_radio.setChecked(False)
        self.ui.approval_radio.setChecked(False)
        self.ui.loss_radio.setChecked(False)
        self.ui.won_radio.setChecked(False)

        # Update radio button check states according to progression
        if status in ["Prospecting", "Qualification", "Negotiating", "Approval", "Closed Loss", "Closed Won"]:
            self.ui.prospecting_radio.setChecked(True)
        if status in ["Qualification", "Negotiating", "Approval", "Closed Loss", "Closed Won"]:
            self.ui.qualification_radio.setChecked(True)
        if status in ["Negotiating", "Approval", "Closed Loss", "Closed Won"]:
            self.ui.negotiating_radio.setChecked(True)
        if status in ["Approval", "Closed Loss", "Closed Won"]:
            self.ui.approval_radio.setChecked(True)
        if status == "Closed Loss":
            self.ui.loss_radio.setChecked(True)
        if status == "Closed Won":
            self.ui.won_radio.setChecked(True)

        # === Dynamic Style Overrides ===
        if status == "Closed Loss":
            # Change to red style
            self.ui.opportunity_status_bar.setStyleSheet("""
                QProgressBar {
                    background-color: #E5E5E5;
                    border: 1px solid #000;
                    border-radius: 10px;
                    text-align: center;
                    height: 20px;
                }
                QProgressBar::chunk {
                    background-color: rgb(255, 93, 78);
                    border-radius: 10px;
                }
            """)

            # Override just the red indicator for loss
            self.ui.loss_radio.setStyleSheet("""
                QRadioButton {
                    background: transparent;
                    color: #fff;
                    border: none;
                }

                QRadioButton::indicator:checked {
                    background-color: rgb(255, 93, 78);
                    border-color: #A3E635;
                }

                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border-radius: 8px;
                    background-color: white;
                }
            """)
        else:
            # Reapply default green styles for progress bar and loss radio
            self.ui.opportunity_status_bar.setStyleSheet("""
                QProgressBar {
                    background-color: #E5E5E5;
                    border: 1px solid #000;
                    border-radius: 10px;
                    text-align: center;
                    height: 20px;
                }
                QProgressBar::chunk {
                    background-color: #A3E635;
                    border-radius: 10px;
                }
            """)

            self.ui.loss_radio.setStyleSheet("""
                QRadioButton {
                    background: transparent;
                    color: #fff;
                    border: none;
                }

                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border-radius: 8px;
                    background-color: white;
                }

                QRadioButton::indicator:checked {
                    background-color: #A3E635;
                    border-color: #A3E635;
                }
            """)

    def set_opportunity_status(self, target_status):
        """Triggered when radio is clicked to confirm and update opportunity status."""

        # Get selected opportunity
        selected_row = self.ui.opportunities_tbl.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an opportunity first!")
            return

        opportunity_id = self.ui.opportunities_tbl.item(selected_row, 0).text()

        # Confirm action
        confirm = QMessageBox.question(
            self,
            "Confirm Status Change",
            f"Are you sure you want to set opportunity status to '{target_status}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        # Update database
        update_query = """
            UPDATE opportunity
            SET opportunity_status = %s
            WHERE opportunity_id = %s
        """
        try:
            self.db_conn.execute_query(update_query, (target_status, opportunity_id))
            QMessageBox.information(self, "Success", "Opportunity status updated successfully.")

            # Refresh status indicators
            self.opportunity_status_indicator(opportunity_id)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update status:\n{e}")

    # def lead_status_indicator(self):
    #     """Updates the progress bar and radio buttons based on the lead status."""
    #     query = """
    #         SELECT l.lead_status
    #         FROM leads l
    #         WHERE l.contact_id = %s
    #     """
    #     lead_data = self.db_conn.fetch_one(query, (self.contact_id,))

    #     if lead_data:
    #         lead_status = lead_data['lead_status']

    #         # Set progress bar value based on lead_status
    #         progress_mapping = {
    #             'Lead': 5,
    #             'Prospecting': 22,
    #             'Qualifications': 39,
    #             'Contacting': 53,
    #             'Negotiating': 68,
    #             'Closed Lost': 83,
    #             'Closed Won': 100
    #         }

    #         progress_value = progress_mapping.get(lead_status, 0)
    #         self.ui.lead_status_bar.setValue(progress_value)  # Correct progress bar name

    #         # Set the radio buttons based on the lead status
    #         # Reset all radio buttons first
    #         self.ui.lead_radio.setChecked(False)
    #         self.ui.prospecting_radio.setChecked(False)
    #         self.ui.qualifications_radio.setChecked(False)
    #         self.ui.contacting_radio.setChecked(False)
    #         self.ui.negotiating_radio.setChecked(False)
    #         self.ui.loss_radio.setChecked(False)
    #         self.ui.won_radio.setChecked(False)

    #         # Set the radio buttons according to the lead's status
    #         if lead_status == 'Lead':
    #             self.ui.lead_radio.setChecked(True)
    #         if lead_status == 'Prospecting':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #         if lead_status == 'Qualifications':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #         if lead_status == 'Contacting':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #         if lead_status == 'Negotiating':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #         if lead_status == 'Closed Lost':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #             self.ui.loss_radio.setChecked(True)
    #         if lead_status == 'Closed Won':
    #             self.ui.lead_radio.setChecked(True)
    #             self.ui.prospecting_radio.setChecked(True)
    #             self.ui.qualifications_radio.setChecked(True)
    #             self.ui.contacting_radio.setChecked(True)
    #             self.ui.negotiating_radio.setChecked(True)
    #             self.ui.loss_radio.setChecked(True)
    #             self.ui.won_radio.setChecked(True)

