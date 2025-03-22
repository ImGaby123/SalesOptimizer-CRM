import os
import sqlite3
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QMainWindow, QMdiArea, QMdiSubWindow, QWidget, QMenuBar,
    QStatusBar, QSizePolicy
)
from PySide6.QtGui import QAction, QBrush, QColor
from PySide6.QtCore import Qt

from views.py.ui_authenticationsystem import Ui_authenticationsystem
from .models_sidebar import SidebarForm
from .models_contacts_landing import ContactsLanding
from views.py.ui_contacts1 import Ui_contacts1
from views.py.ui_contacts4 import Ui_contacts4
from views.py.ui_contacts_create import Ui_contacts_create

# Setup database connection path (persistent connection in this example)
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, '..', 'datas', 'mydb.db')
conn = sqlite3.connect(db_path)

#############################
# AuthenticationSystem Class
#############################
class AuthenticationSystem(QDialog, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_authenticationsystem()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.login_button.clicked.connect(self.login)
        self.ui.createacc_button.clicked.connect(lambda: self.switch_page(1))
        self.ui.signup_button.clicked.connect(self.signup)
        self.ui.back2login_button.clicked.connect(lambda: self.switch_page(0))
        self.ui.password_input_2.textChanged.connect(self.validate_password)
        self.show()

    def switch_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def login(self):
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()

        if not username or not password:
            self.ui.uservalidation_label.setText("All fields are required")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            self.open_mainwindow()
        else:
            self.ui.passvalidation_label.setText("Username or password is incorrect")
        conn.close()

    def validate_password(self):
        password = self.ui.password_input_2.text().strip()
        messages = []
        messages.append("✅ At least 8 characters." if len(password) >= 8 else "🔴 Must be at least 8 characters.")
        messages.append("✅ Contains a lowercase letter." if any(c.islower() for c in password) else "🔴 Must contain a lowercase letter.")
        messages.append("✅ Contains an uppercase letter." if any(c.isupper() for c in password) else "🔴 Must contain an uppercase letter.")
        messages.append("✅ Contains a number or symbol." if any(c.isdigit() for c in password) or any(c in '!@#$%^&*()' for c in password) else "🔴 Must contain a number or a symbol (!@#$%^&*()).")
        self.ui.validation_label.setText("\n".join(messages))

    def signup(self):
        username = self.ui.username_input_2.text().strip()
        password = self.ui.password_input_2.text().strip()
        confirm_password = self.ui.confirmpass_input.text().strip()

        if not username or not password or not confirm_password:
            self.ui.validation_label.setText("All fields are required")
            return
        if password != confirm_password:
            self.ui.validation_label.setText("Passwords do not match")
            return
        if "🔴" in self.ui.validation_label.text():
            QMessageBox.warning(self, "Invalid Password", "Please meet all password requirements before signing up.")
            return

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ?", (username,))
        if cursor.fetchone():
            self.ui.validation_label.setText("Username already taken")
            conn.close()
            return

        cursor.execute("INSERT INTO accounts_tbl (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Account created successfully!")
        self.switch_page(0)

    def open_mainwindow(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.accept()

###################################
# MainWindow Class (MDI Management)
###################################
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRM | SalesOptimizer")

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        self.mdi_area.setBackground(QBrush(QColor(255, 255, 255)))

        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))

        self.transposed = False  # Flag for swapping sidebar/mainform
        self.sidebar_visible = True
        self.create_menu()
        self.create_subwindows()
        self.showMaximized()

    def create_menu(self):
        menu_bar = self.menuBar()
        open_menu = menu_bar.addMenu("Open")
        window_menu = menu_bar.addMenu("Window")

        self.sidebar_action = QAction("Sidebar", self, checkable=True)
        self.sidebar_action.setChecked(True)
        self.sidebar_action.triggered.connect(self.toggle_sidebar)

        self.mainform_action = QAction("MainForm", self, checkable=True)
        self.mainform_action.setChecked(True)
        self.mainform_action.triggered.connect(self.toggle_mainform)

        open_menu.addAction(self.sidebar_action)
        open_menu.addAction(self.mainform_action)

        realign_action = QAction("Realign Windows", self)
        realign_action.triggered.connect(self.realign_subwindows)
        transpose_action = QAction("Transpose Windows", self)
        transpose_action.triggered.connect(self.transpose_subwindows)

        window_menu.addAction(realign_action)
        window_menu.addAction(transpose_action)

    def create_subwindows(self):
        screen_width = self.screen().availableGeometry().width()
        screen_height = self.screen().availableGeometry().height() - self.menuBar().height() - self.statusBar().height()

        self.sidebar = SidebarForm()
        self.sidebar.changeForm.connect(self.load_form)

        # Create sidebar and mainform subwindows with full expansion
        self.left_subwin = self.create_mdi_subwindow(self.sidebar, int(screen_width * 0.1), screen_height, 0, 0)
        self.right_subwin = self.create_mdi_subwindow(QWidget(), int(screen_width * 0.9), screen_height, int(screen_width * 0.1), 0)
        self.right_subwin.closeEvent = self.handle_right_close
        self.left_subwin.closeEvent = self.handle_left_close

    def load_form(self, form_name):
        form_map = {
            "Home": Ui_contacts1,
            "Pipeline": Ui_contacts1,
            "Funnel": Ui_contacts_create,
            "Leads": Ui_contacts4,
            "Contacts": ContactsLanding,
            "Logout": None
        }

        if form_name not in form_map or form_map[form_name] is None:
            QMessageBox.warning(self, "Invalid Action", f"No form assigned for {form_name}.")
            return

        target_subwin = self.right_subwin if not self.transposed else self.left_subwin

        if target_subwin.widget():
            target_subwin.widget().deleteLater()
            target_subwin.setWidget(None)

        form_class = form_map[form_name]
        new_widget = form_class() if issubclass(form_class, QWidget) else MainForm(form_class)
        target_subwin.setWidget(new_widget)
        target_subwin.show()


    def create_mdi_subwindow(self, widget, width, height, x, y):
        subwin = QMdiSubWindow()
        subwin.setWidget(widget)
        subwin.setWindowTitle("")
        subwin.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        subwin.resize(width, height)
        self.mdi_area.addSubWindow(subwin)
        subwin.move(x, y)
        subwin.show()
        return subwin

    def realign_subwindows(self):
        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()
        if self.sidebar_visible:
            left_width = int(screen_width * 0.1)
            right_width = int(screen_width * 0.9)
        else:
            left_width = 0
            right_width = screen_width
        if self.transposed:
            self.left_subwin.setGeometry(0, 0, right_width, screen_height)
            self.right_subwin.setGeometry(right_width, 0, left_width, screen_height)
        else:
            self.left_subwin.setGeometry(0, 0, left_width, screen_height)
            self.right_subwin.setGeometry(left_width, 0, right_width, screen_height)

    def transpose_subwindows(self):
        self.transposed = not self.transposed
        self.left_subwin, self.right_subwin = self.right_subwin, self.left_subwin
        self.realign_subwindows()

    def toggle_sidebar(self):
        sidebar_subwin = self.left_subwin if not self.transposed else self.right_subwin
        if self.sidebar_visible:
            sidebar_subwin.hide()
            self.sidebar_visible = False
        else:
            sidebar_subwin.show()
            self.sidebar_visible = True
        self.sidebar_action.setChecked(self.sidebar_visible)
        self.realign_subwindows()

    def toggle_mainform(self):
        if self.right_subwin is not None:
            self.right_subwin.setVisible(not self.right_subwin.isVisible())
            self.mainform_action.setChecked(self.right_subwin.isVisible())

    def handle_left_close(self, event):
        self.sidebar_visible = False
        self.sidebar_action.setChecked(False)
        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()
        # Identify which subwindow is sidebar and which is mainform
        sidebar_subwin = self.left_subwin if not self.transposed else self.right_subwin
        mainform_subwin = self.right_subwin if not self.transposed else self.left_subwin
        sidebar_subwin.hide()
        mainform_subwin.setGeometry(0, 0, screen_width, screen_height)
        self.realign_subwindows()
        event.ignore()

    def handle_right_close(self, event):
        self.mainform_action.setChecked(False)
        event.accept()

    def resizeEvent(self, event):
        self.realign_subwindows()
        super().resizeEvent(event)

#################################
# MainForm Wrapper for UI Scaling
#################################
class MainForm(QWidget):
    def __init__(self, ui_class):
        super().__init__()
        self.ui = ui_class()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = self.find_main_layout()
        if layout:
            self.setLayout(layout)

    def find_main_layout(self):
        for attr_name in ["gridLayout", "verticalLayout", "horizontalLayout", "formLayout"]:
            layout = getattr(self.ui, attr_name, None)
            if layout:
                return layout
        return None

#################################
# MDIManager for Centralized Loading
#################################
class MDIManager:
    @staticmethod
    def load_into_mdi(widget_class):
        from PySide6.QtWidgets import QApplication
        from models.models_authentication import MainWindow

        main_window = next((w for w in QApplication.instance().topLevelWidgets() if isinstance(w, MainWindow)), None)
        if not main_window:
            print("Error: MainWindow not found!")
            return

        target_subwin = main_window.right_subwin if not main_window.transposed else main_window.left_subwin
        if target_subwin.widget():
            target_subwin.widget().deleteLater()
            target_subwin.setWidget(None)

        new_widget = widget_class()
        target_subwin.setWidget(new_widget)
        target_subwin.show()
