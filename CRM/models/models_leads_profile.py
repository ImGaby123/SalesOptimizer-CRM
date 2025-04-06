from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QCheckBox, QHeaderView, QLineEdit, QMessageBox, QApplication, QMenu
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QAction
from views.py.ui_leads_profile import Ui_leads_profile
from datas.db_connection import DB_Connection

class LeadsProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leads_profile()
        self.ui.setupUi(self)

        # ✅ Initialize database connection
        self.db_conn = DB_Connection()
