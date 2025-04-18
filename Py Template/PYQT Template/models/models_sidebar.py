from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal
from views.py.ui_sidebar import Ui_sidebar


class SidebarForm(QWidget):
    changeForm = Signal(str)  # Signal to notify MainWindow which form to load

    def __init__(self):
        super().__init__()
        self.ui = Ui_sidebar()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(self.ui.verticalLayout)

        # Connect buttons to signal with form name
        self.ui.home_btn.clicked.connect(lambda: self.changeForm.emit("Home"))
        self.ui.pipeline_btn.clicked.connect(lambda: self.changeForm.emit("Pipeline"))
        self.ui.funnel_btn.clicked.connect(lambda: self.changeForm.emit("Funnel"))
        self.ui.leads_btn.clicked.connect(lambda: self.changeForm.emit("Leads"))
        self.ui.contacts_btn.clicked.connect(lambda: self.changeForm.emit("Contacts"))
        self.ui.logout_btn.clicked.connect(lambda: self.changeForm.emit("Logout"))
