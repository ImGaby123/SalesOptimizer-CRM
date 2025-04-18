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

        self.db_conn = DB_Connection()

        self.contact_info()
        self.opportunities_table()
        self.all_opportunity_cost()

        self.ui.won_btn.clicked.connect(lambda: self.buttons_opportunity_cost("Closed Won"))
        self.ui.loss_btn.clicked.connect(lambda: self.buttons_opportunity_cost("Closed Loss"))

        self.ui.add_btn.clicked.connect(self.add_opportunity)
        self.ui.edit_btn.clicked.connect(self.edit_opportunity)
        self.ui.delete_btn.clicked.connect(self.delete_opportunity)

        self.ui.add_campaign_btn.clicked.connect(self.add_campaign)
        self.ui.edit_campaign_btn.clicked.connect(self.edit_campaign)
        self.ui.delete_campaign_btn.clicked.connect(self.delete_campaign)

        self.ui.qualification_radio.clicked.connect(lambda: self.set_opportunity_status("Qualification"))
        self.ui.negotiating_radio.clicked.connect(lambda: self.set_opportunity_status("Negotiating"))
        self.ui.approval_radio.clicked.connect(lambda: self.set_opportunity_status("Approval"))

        self.ui.full_info_lbl.mousePressEvent = lambda event: self.view_contact_info()
        self.ui.back_btn.clicked.connect(self.go_back)

    # ------------------------
    # Navigation and UI Setup
    # ------------------------
    def go_back(self):
        from models.models_authentication import MDIManager
        from models.models_leads_landing import LeadsLanding
        MDIManager.load_into_mdi(LeadsLanding)

    def view_contact_info(self):
        from models.models_authentication import MDIManager
        from models.models_contacts_view import ContactsView

        if not self.contact_id:
            return

        MDIManager.load_into_mdi(lambda: ContactsView(self.contact_id))

    # ------------------------
    # Contact Information
    # ------------------------
    def contact_info(self):
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
            self.ui.lead_source_value_lbl.setText(contact_data['source_name'] if contact_data['source_name'] else "N/A")

    # ------------------------
    # Opportunities Management
    # ------------------------
    def opportunities_table(self):
        self.ui.opportunities_tbl.setRowCount(0)
        self.ui.opportunities_tbl.setColumnCount(2)
        self.ui.opportunities_tbl.setHorizontalHeaderLabels(["ID", "Opportunity Title"])
        self.ui.opportunities_tbl.setColumnHidden(0, True)

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

        table = self.ui.opportunities_tbl
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.cellClicked.connect(self.load_opportunity_details)

    def load_opportunity_details(self, row, column):
        opportunity_id_item = self.ui.opportunities_tbl.item(row, 0)
        if not opportunity_id_item:
            return

        opportunity_id = opportunity_id_item.text()

        query = """
            SELECT opportunity_title, opportunity_cost, date, opportunity_details, opportunity_status
            FROM opportunity
            WHERE opportunity_id = %s
        """
        data = self.db_conn.fetch_one(query, (opportunity_id,))
        if data:
            self.ui.opportunity_title_lbl.setText(data["opportunity_title"] or "N/A")
            self.ui.leadinfohead_lbl_3.setText(data["opportunity_title"] or "N/A")
            self.ui.opportunity_name.setText(data["opportunity_title"] or "N/A")
            self.ui.opportunity_cost_lbl.setText(f"{data['opportunity_cost']:.2f}" if data["opportunity_cost"] else "0.00")
            self.ui.opportunity_date_lbl.setText(data["date"].strftime("%Y-%m-%d") if data["date"] else "N/A")
            self.ui.opportunity_details_lbl.setText(data["opportunity_details"] or "N/A")

        self.opportunity_status_indicator(opportunity_id)
        self.selected_opportunity_cost()
        self.toggle_opportunity_cost_buttons(data["opportunity_status"])
        self.campaign_tbl(opportunity_id)

    def add_opportunity(self):
        from models.models_add_opportunity import AddOpportunity
        dialog = AddOpportunity(self.contact_id, self)
        dialog.exec()

    def edit_opportunity(self):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return
        from models.models_edit_opportunity import EditOpportunity
        dialog = EditOpportunity(self.contact_id, opportunity_id, self)
        dialog.exec()

    def delete_opportunity(self):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return

        confirm = QMessageBox.question(
            self, "Confirm Deletion", "Are you sure you want to delete opportunity?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        try:
            delete_query = "DELETE FROM opportunity WHERE opportunity_id = %s"
            self.db_conn.execute_query(delete_query, (opportunity_id,))
            QMessageBox.information(self, "Success", "Opportunity deleted successfully.")
            self.opportunities_table()
            self.reset_opportunity_details()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete opportunity:\n{e}")

    def get_selected_opportunity_id(self):
        row = self.ui.opportunities_tbl.currentRow()
        if row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an opportunity first!")
            return None

        item = self.ui.opportunities_tbl.item(row, 0)
        if not item:
            QMessageBox.warning(self, "Error", "Unable to find the opportunity ID.")
            return None

        return item.text()

    def reset_opportunity_details(self):
        self.ui.opportunity_title_lbl.setText("N/A")
        self.ui.opportunity_cost_lbl.setText("0.00")
        self.ui.opportunity_date_lbl.setText("N/A")
        self.ui.opportunity_details_lbl.setText("N/A")

    # ------------------------
    # Status and Cost Handling
    # ------------------------
    def set_opportunity_status(self, target_status):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Status Change",
            f"Are you sure you want to set opportunity status to '{target_status}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        try:
            update_query = """
                UPDATE opportunity
                SET opportunity_status = %s
                WHERE opportunity_id = %s
            """
            self.db_conn.execute_query(update_query, (target_status, opportunity_id))
            QMessageBox.information(self, "Success", "Opportunity status updated successfully.")
            self.opportunity_status_indicator(opportunity_id)
            self.selected_opportunity_cost()
            self.toggle_opportunity_cost_buttons(target_status)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update status:\n{e}")

    def opportunity_status_indicator(self, opportunity_id):
        query = "SELECT opportunity_status FROM opportunity WHERE opportunity_id = %s"
        data = self.db_conn.fetch_one(query, (opportunity_id,))
        if not data:
            return

        status = data["opportunity_status"]

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

        # Reset radio buttons
        radios = [
            self.ui.prospecting_radio,
            self.ui.qualification_radio,
            self.ui.negotiating_radio,
            self.ui.approval_radio,
            self.ui.loss_radio,
            self.ui.won_radio,
        ]
        for radio in radios:
            radio.setChecked(False)

        # Check appropriate radios based on status
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

        # Styles
        red_progress_style = """
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
        """

        green_progress_style = """
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
        """

        red_radio_style = """
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
                background-color: rgb(255, 93, 78);
                border-color: #A3E635;
            }
        """

        green_radio_style = """
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
        """

        if status == "Closed Loss":
            self.ui.opportunity_status_bar.setStyleSheet(red_progress_style)
            for radio in [
                self.ui.prospecting_radio,
                self.ui.qualification_radio,
                self.ui.negotiating_radio,
                self.ui.approval_radio,
                self.ui.loss_radio,
            ]:
                radio.setStyleSheet(red_radio_style)
        else:
            self.ui.opportunity_status_bar.setStyleSheet(green_progress_style)
            for radio in [
                self.ui.prospecting_radio,
                self.ui.qualification_radio,
                self.ui.negotiating_radio,
                self.ui.approval_radio,
                self.ui.loss_radio,
            ]:
                radio.setStyleSheet(green_radio_style)

    def all_opportunity_cost(self):
        query = """
            SELECT opportunity_status, SUM(opportunity_cost) AS total_cost
            FROM opportunity
            WHERE contact_id = %s
            GROUP BY opportunity_status
        """
        results = self.db_conn.fetch_all(query, (self.contact_id,))
        pending_total = 0.0
        won_total = 0.0
        loss_total = 0.0

        for row in results:
            status = row["opportunity_status"]
            cost = float(row["total_cost"] or 0.0)
            if status in ("Prospecting", "Qualification", "Negotiating", "Approval"):
                pending_total += cost
            elif status == "Closed Won":
                won_total += cost
            elif status == "Closed Loss":
                loss_total += cost

        self.ui.pending_lbl.setText(f"₱{pending_total:,.2f}")
        self.ui.won_lbl.setText(f"₱{won_total:,.2f}")
        self.ui.loss_lbl.setText(f"₱{loss_total:,.2f}")

    def selected_opportunity_cost(self):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return

        query = """
            SELECT opportunity_cost, opportunity_status
            FROM opportunity
            WHERE opportunity_id = %s
        """
        data = self.db_conn.fetch_one(query, (opportunity_id,))
        if not data:
            return

        cost = data["opportunity_cost"] or 0.0
        status = data["opportunity_status"]

        self.ui.pending_lbl.setText("₱0.00")
        self.ui.won_lbl.setText("₱0.00")
        self.ui.loss_lbl.setText("₱0.00")

        if status in ("Prospecting", "Qualification", "Negotiating", "Approval"):
            self.ui.pending_lbl.setText(f"₱{cost:,.2f}")
        elif status == "Closed Won":
            self.ui.won_lbl.setText(f"₱{cost:,.2f}")
        elif status == "Closed Loss":
            self.ui.loss_lbl.setText(f"₱{cost:,.2f}")

    def toggle_opportunity_cost_buttons(self, status):
        if status == "Closed Won":
            self.ui.won_btn.setEnabled(False)
            self.ui.loss_btn.setEnabled(True)
        elif status == "Closed Loss":
            self.ui.won_btn.setEnabled(True)
            self.ui.loss_btn.setEnabled(False)
        else:
            self.ui.won_btn.setEnabled(True)
            self.ui.loss_btn.setEnabled(True)

    def buttons_opportunity_cost(self, to_status):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return

        label = "Closed Won" if to_status == "Closed Won" else "Closed Loss"

        confirm = QMessageBox.question(
            self,
            f"Confirm {label}",
            f"Are you sure you want to set this opportunity to {label}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                query = "UPDATE opportunity SET opportunity_status = %s WHERE opportunity_id = %s"
                self.db_conn.execute_query(query, (to_status, opportunity_id))
                QMessageBox.information(self, "Success", f"Opportunity set to {label}.")
                self.selected_opportunity_cost()
                self.opportunity_status_indicator(opportunity_id)
                self.toggle_opportunity_cost_buttons(to_status)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to update status:\n{e}")

    # ------------------------
    # Campaign Management
    # ------------------------
    def campaign_tbl(self, opportunity_id):
        query = """
            SELECT
                ct.campaign_id,
                o.opportunity_title AS Opportunity,
                ct.action AS Action,
                ct.type AS Type,
                DATE_FORMAT(ct.campaign_date, '%Y-%m-%d') AS Date,  -- Format date to 'yyyy-mm-dd'
                ct.campaign_details AS Details
            FROM campaign_timeline ct
            JOIN opportunity o ON o.opportunity_id = ct.opportunity_id
            WHERE ct.opportunity_id = %s
            ORDER BY ct.campaign_date DESC
        """
        results = self.db_conn.fetch_all(query, (opportunity_id,))
        if results is None:
            QMessageBox.warning(self, "Error", "Failed to load campaigns.")
            return

        self.ui.campaign_tbl.setRowCount(len(results))
        self.ui.campaign_tbl.setColumnCount(5)
        self.ui.campaign_tbl.setHorizontalHeaderLabels(["Opportunity", "Action", "Type", "Date Created", "Details"])
        self.ui.campaign_tbl.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.campaign_tbl.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.campaign_tbl.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.campaign_tbl.verticalHeader().setVisible(False)  # ✅ remove 1.. row numbers
        self.ui.campaign_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.campaign_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        for row, campaign in enumerate(results):
            self.ui.campaign_tbl.setItem(row, 0, QTableWidgetItem(campaign["Opportunity"]))
            self.ui.campaign_tbl.setItem(row, 1, QTableWidgetItem(campaign["Action"]))
            self.ui.campaign_tbl.setItem(row, 2, QTableWidgetItem(campaign["Type"]))
            self.ui.campaign_tbl.setItem(row, 3, QTableWidgetItem(campaign["Date"]))  # Now in 'yyyy-mm-dd'
            self.ui.campaign_tbl.setItem(row, 4, QTableWidgetItem(campaign["Details"]))

            # Optional: Store campaign_id as hidden metadata
            self.ui.campaign_tbl.item(row, 0).setData(Qt.UserRole, campaign["campaign_id"])

    def get_selected_campaign_id(self):
        row = self.ui.campaign_tbl.currentRow()
        if row == -1:
            QMessageBox.warning(self, "No Selection", "Select a Campaign First!")
            return None

        item = self.ui.campaign_tbl.item(row, 0)
        return item.data(Qt.UserRole)

    def add_campaign(self):
        opportunity_id = self.get_selected_opportunity_id()
        if not opportunity_id:
            return  # Stop if no selection

        from models.models_add_campaign import AddCampaign
        dialog = AddCampaign(self.contact_id, opportunity_id, self)
        dialog.exec()

    def edit_campaign(self):
        campaign_id = self.get_selected_campaign_id()
        opportunity_id = self.get_selected_opportunity_id()

        if not campaign_id or not opportunity_id:
            return

        from models.models_edit_campaign import EditCampaign
        dialog = EditCampaign(self.contact_id, opportunity_id, campaign_id, self)
        dialog.exec()

        # Reload campaigns after edit
        self.campaign_tbl(opportunity_id)

    def delete_campaign(self):
        campaign_id = self.get_selected_campaign_id()
        opportunity_id = self.get_selected_opportunity_id()

        if not campaign_id or not opportunity_id:
            return

        confirm = QMessageBox.question(
            self,
            "Delete Confirmation",
            "Are you sure you want to delete this Campaign?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            from datas.db_connection import DB_Connection
            db = DB_Connection()
            query = "DELETE FROM campaign_timeline WHERE campaign_id = %s"
            if db.execute_query(query, (campaign_id,)):
                QMessageBox.information(self, "Deleted", "Campaign deleted successfully.")
                self.campaign_tbl(opportunity_id)
            else:
                QMessageBox.critical(self, "Error", "Failed to delete campaign.")




