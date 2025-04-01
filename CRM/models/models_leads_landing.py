from PySide6.QtWidgets import QWidget, QSizePolicy
from views.py.ui_leads_landing import Ui_leads_landing


class LeadsLanding(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leads_landing()
        self.ui.setupUi(self)
