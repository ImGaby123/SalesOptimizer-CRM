from views.py.ui_market_dashboard import Ui_Form

from PySide6.QtWidgets import QMainWindow, QWidget


class marketdashboard(QWidget, Ui_Form):

    # -------------------------- Main Window content
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)