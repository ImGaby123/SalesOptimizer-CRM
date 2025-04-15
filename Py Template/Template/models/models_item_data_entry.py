from PySide6.QtWidgets import (
    QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QCheckBox, QHeaderView, QLineEdit, QMessageBox, QApplication, QMenu
)
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QAction

# item Pages References
from views.py.ui_item_data_entry import Ui_item_data_entry


class ItemDataEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_item_data_entry()
        self.ui.setupUi(self)

        # Back Action Button
        self.ui.back_btn.clicked.connect(self.return_page)


    def return_page(self):
        print("Dobber Man")
        from models.models_mainwindow import MDIManager
        from models.models_item_table_view import ItemTableView
        MDIManager.load_into_mdi(ItemTableView)
