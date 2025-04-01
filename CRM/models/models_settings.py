from PySide6.QtWidgets import (QWidget, QSizePolicy)
from views.py.ui_settings import Ui_settings


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
