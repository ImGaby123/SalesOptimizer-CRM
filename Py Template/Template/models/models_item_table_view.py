from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QCheckBox, QHeaderView, QLineEdit, QMessageBox, QApplication, QMenu
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QAction

# item Pages References
from views.py.ui_item_table_view import Ui_item_table_view
from models.models_item_data_entry import ItemDataEntry




class ItemTableView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_item_table_view()
        self.ui.setupUi(self)

        # Properly expand columns
        self.ui.items_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.add_btn.clicked.connect(self.add_item)


    def add_item(self):
        print("Dobber Man")
        #Opens the Contacts Create form inside the MDI subwindow.
        from models.models_mainwindow import MDIManager
        MDIManager.load_into_mdi(ItemDataEntry)
