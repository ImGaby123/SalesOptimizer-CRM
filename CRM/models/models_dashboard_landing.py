from PySide6.QtWidgets import (QWidget, QSizePolicy)
from views.py.ui_dashboard_landing import Ui_dashboard


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def total_leads(self):
        filter_text = self.ui.lead_combo.currentText()

        query = "SELECT COUNT(*) AS total FROM leads"
        if filter_text == "Last Week":
            query += " WHERE created_at >= NOW() - INTERVAL 1 WEEK"
        elif filter_text == "Last Month":
            query += " WHERE created_at >= NOW() - INTERVAL 1 MONTH"
        elif filter_text == "Last Year":
            query += " WHERE created_at >= NOW() - INTERVAL 1 YEAR"

        result = self.db_conn.fetch_one(query)
        total = result["total"] if result else 0
        self.ui.total_leads_qty_lbl.setText(str(total))
