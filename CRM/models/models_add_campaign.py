from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (QWidget, QSizePolicy)
from views.py.ui_add_campaign import Ui_add_campaign

class AddCampaign(QDialog):
    def __init__(self, contact_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_add_campaign()
        self.contact_id = contact_id
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
