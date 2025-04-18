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

        # Store all buttons in a dictionary
        self.buttons = {
            "Dashboard": self.ui.dashboard_btn,
            "Contacts": self.ui.contacts_btn,
            "Leads": self.ui.leads_btn,
            "Settings": self.ui.settings_btn,
            "Logout": self.ui.logout_btn
        }

        # Apply default styles and connect buttons
        for name, button in self.buttons.items():
            button.setStyleSheet(self.get_default_style())  # Set default style
            button.clicked.connect(lambda checked, name=name: self.set_active_button(name))

        self.set_active_button("Dashboard")  # Set "Dashboard" as active by default

    def get_default_style(self):
        """ Default (inactive) button style: black background, no border, white text """
        return """
            QPushButton {
                background-color: #171717;
                border: none;
                padding: 8px;
                color: rgb(220, 220, 220);
                text-align: left;
            }
            QPushButton:hover {
                background-color: rgb(30, 30, 30);
                color: rgb(255, 255, 255);
            }
            QPushButton:pressed {
                background-color: rgb(20, 20, 20);
            }
        """

    def get_active_style(self):
        """ Active button style: lighter grey background, bold white text, and left border """
        return """
            QPushButton {
                background-color: rgb(30, 30, 30);  /* Lighter than inactive button */
                border: none;
                padding: 8px;
                color: rgb(255, 255, 255);
                text-align: left;
                font-weight: bold;
                border-left: 5px solid rgb(80, 80, 80);  /* White left border */
            }
            QPushButton:hover {
                background-color: rgb(50, 50, 50);  /* Lighter hover color */
            }
            QPushButton:pressed {
                background-color: rgb(30, 30, 30);  /* Lighter pressed color */
            }
        """

    def set_active_button(self, active_name):
        """ Updates button styles to reflect active selection """
        for name, button in self.buttons.items():
            if name == active_name:
                button.setStyleSheet(self.get_active_style())  # Apply active style
            else:
                button.setStyleSheet(self.get_default_style())  # Revert others to default

        self.changeForm.emit(active_name)  # Emit signal to change form
