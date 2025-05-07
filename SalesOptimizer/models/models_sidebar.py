from PySide6.QtWidgets import QWidget, QSizePolicy
from PySide6.QtCore import Signal
from views.py.ui_sidebar import Ui_sidebar

class SidebarForm(QWidget):
    changeForm = Signal(str)  # Signal to notify MainWindow which form to load

    def __init__(self):
        super().__init__()
        self.ui = Ui_sidebar()
        self.ui.setupUi(self)
        self.ui.home_btn.hide()

        # Sizing and Layout
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(self.ui.verticalLayout)

        # Store all buttons in a dictionary
        self.buttons = {
            "Home": self.ui.home_btn,
            "Item1": self.ui.item1_btn,
            "Item2": self.ui.item2_btn
        }

        # Apply default styles and connect buttons
        for name, button in self.buttons.items():
            button.clicked.connect(lambda checked, name=name: self.set_active_button(name))


        # Initial Page to be shown Upon Entry
        self.set_active_button("Home")


    def set_active_button(self, active_name):
        self.changeForm.emit(active_name)  # Emit signal to change form
