from PySide6.QtWidgets import QWidget
from views.py.ui_contacts_create import Ui_contacts_create
from PySide6.QtWidgets import QWidget, QSizePolicy

class ContactsCreate(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts_create()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
