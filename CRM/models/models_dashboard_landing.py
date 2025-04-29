from PySide6.QtWidgets import QWidget, QSizePolicy, QTableWidgetItem, QHeaderView
from PySide6.QtCore import QDate
from views.py.ui_dashboard_landing import Ui_dashboard
from datas.db_connection import DB_Connection

from datetime import datetime, timedelta

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.db = DB_Connection()

        # Load initial data
        self.sort_details()
        self.del_lead_priority_table()
        header = self.ui.lead_tbl.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Connect sort combo change
        self.ui.sort_combo.currentIndexChanged.connect(self.sort_details)

    def crm_details(self, date_filter=None):
        """Update the dashboard counters based on optional date filter."""
        date_condition = ""
        params = []

        if date_filter:
            date_condition = "WHERE created_at >= %s"
            params.append(date_filter)

        # Leads count
        leads_query = f"SELECT COUNT(*) AS total FROM leads {date_condition}"
        leads_result = self.db.fetch_one(leads_query, tuple(params))
        self.ui.leads_lbl.setText(str(leads_result["total"] if leads_result else 0))

        # Opportunities count
        opp_query = f"SELECT COUNT(*) AS total FROM opportunity {date_condition}"
        opp_result = self.db.fetch_one(opp_query, tuple(params))
        self.ui.opportunities_lbl.setText(str(opp_result["total"] if opp_result else 0))

        # Closed Won count
        won_query = f"""
            SELECT COUNT(*) AS total FROM opportunity
            WHERE opportunity_status = 'Closed Won'
            {"AND created_at >= %s" if date_filter else ""}
        """
        won_params = (date_filter,) if date_filter else ()
        won_result = self.db.fetch_one(won_query, won_params)
        self.ui.won_lbl.setText(str(won_result["total"] if won_result else 0))

        # Closed Loss count
        loss_query = f"""
            SELECT COUNT(*) AS total FROM opportunity
            WHERE opportunity_status = 'Closed Loss'
            {"AND created_at >= %s" if date_filter else ""}
        """
        loss_params = (date_filter,) if date_filter else ()
        loss_result = self.db.fetch_one(loss_query, loss_params)
        self.ui.loss_lbl.setText(str(loss_result["total"] if loss_result else 0))

    def sort_details(self):
        """Apply date range based on selected sort option."""
        selected = self.ui.sort_combo.currentText()
        today = datetime.today()

        if selected == "Last 3 Days":
            date_filter = today - timedelta(days=3)
        elif selected == "Last 7 Days":
            date_filter = today - timedelta(days=7)
        elif selected == "Last 30 Days":
            date_filter = today - timedelta(days=30)
        else:
            # "Total" or any fallback
            date_filter = None

        self.crm_details(date_filter)

    def del_lead_priority_table(self):
        """Populate lead_tbl with contact full name and lead_score, ordered by lead_score descending."""
        query = """
            SELECT
                CONCAT(c.first_name, ' ', c.last_name) AS name,
                l.lead_score
            FROM leads l
            JOIN contact c ON l.contact_id = c.contact_id
            ORDER BY l.lead_score DESC
        """
        results = self.db.fetch_all(query)

        table = self.ui.lead_tbl
        table.setRowCount(0)  # Clear previous rows

        if not results:
            return

        # Set headers explicitly to 'Leads' and 'Lead Score'
        headers = ["Leads", "Lead Score"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        # Fill the table with the data
        for row_idx, row in enumerate(results):
            table.insertRow(row_idx)
            table.setItem(row_idx, 0, QTableWidgetItem(str(row["name"]) if row["name"] is not None else ""))
            table.setItem(row_idx, 1, QTableWidgetItem(str(row["lead_score"]) if row["lead_score"] is not None else ""))


