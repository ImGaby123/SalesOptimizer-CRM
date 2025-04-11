from PySide6.QtWidgets import (QWidget, QSizePolicy)
from views.py.ui_dashboard_landing import Ui_dashboard


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
