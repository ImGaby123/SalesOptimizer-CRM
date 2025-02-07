import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QMenuBar, QStatusBar, QWidget, QSizePolicy
from PySide6.QtCore import Qt
from ui_authenticationsystem import Ui_authenticationsystem
from ui_sidebar import Ui_sidebar

class AuthenticationSystem(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_authenticationsystem()
        self.ui.setupUi(self)

        # StackedWidget
        self.stackedWidget = self.ui.stackedWidget
        self.stackedWidget.setCurrentIndex(0)  # Ensure login page is shown first

        # Login Widgets
        self.username_input = self.ui.username_input
        self.password_input = self.ui.password_input
        self.uservalidation_label = self.ui.uservalidation_label
        self.passvalidation_label = self.ui.passvalidation_label
        self.login_button = self.ui.login_button
        self.createacc_button = self.ui.createacc_button

        # Signup Widgets
        self.username_input_2 = self.ui.username_input_2
        self.password_input_2 = self.ui.password_input_2
        self.confirmpass_input = self.ui.confirmpass_input
        self.validation_label = self.ui.validation_label
        self.signup_button = self.ui.signup_button

        # Button Connections
        self.login_button.clicked.connect(self.login)
        self.createacc_button.clicked.connect(self.show_signup)
        self.signup_button.clicked.connect(self.signup)

        self.show()

    def show_signup(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_login(self):
        self.stackedWidget.setCurrentIndex(0)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username:
            self.uservalidation_label.setText("Username field is required")
            return
        if not password:
            self.passvalidation_label.setText("Password field is required")
            return

        conn = sqlite3.connect(r"C:\Users\Administrator\Documents\QTCreatorProjects\SalesOptimizer-CRM\CRM\mydb.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            QMessageBox.information(self, "Success", "Login successful!")
            self.open_mainwindow()
        else:
            self.passvalidation_label.setText("Username or password is incorrect")

    def signup(self):
        username = self.username_input_2.text().strip()
        password = self.password_input_2.text().strip()
        confirm_password = self.confirmpass_input.text().strip()

        if not username:
            self.validation_label.setText("Username field is required")
            return
        if not password:
            self.validation_label.setText("Password field is required")
            return
        if not confirm_password:
            self.validation_label.setText("Confirm password field is required")
            return

        if len(password) < 8 or not any(c.islower() for c in password) or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in '!@#$%^&*()' for c in password):
            self.validation_label.setText("Password must contain at least 1 lowercase, 1 uppercase, 1 number, and 1 symbol")
            return

        if password != confirm_password:
            self.validation_label.setText("Passwords do not match")
            return

        conn = sqlite3.connect(r"C:\Users\QCU\Desktop\SalesOptimizer_CRM\AuthenticationSystem\AuthenticationSystem\mydb.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ?", (username,))
        if cursor.fetchone():
            self.validation_label.setText("Username already taken")
            conn.close()
            return

        cursor.execute("INSERT INTO accounts_tbl (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Account created successfully!")
        self.show_login()

    def open_mainwindow(self):
        """ Open MainWindow after successful login """
        self.main_window = MainWindow()  # Create MainWindow instance
        self.main_window.show()
        self.accept()  # Close login dialog

class SidebarForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sidebar()
        self.ui.setupUi(self)

        # Ensure the sidebar widget resizes with its parent subwindow
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set layout for sidebar to fill parent space
        self.setLayout(self.ui.verticalLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup menu bar and status bar
        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))

        # Set the MDI Area manually
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # Create and add subwindows
        self.create_subwindows()

        # Show maximized by default
        self.showMaximized()

    def create_subwindows(self):
        """ Create two subwindows with a 10:90 split inside the loaded MDI area. """
        screen_width = self.screen().availableGeometry().width()
        screen_height = self.screen().availableGeometry().height() - self.menuBar().height() - self.statusBar().height()

        left_width = int(screen_width * 0.1)  # 10% width
        right_width = int(screen_width * 0.9)  # 90% width

        # Left Subwindow (10%) with Sidebar UI
        self.sidebar = SidebarForm()  # Load sidebar UI
        self.left_subwin = QMdiSubWindow()
        self.left_subwin.setWidget(self.sidebar)
        self.left_subwin.setWindowTitle("Sidebar")
        self.left_subwin.resize(left_width, screen_height)
        self.mdi_area.addSubWindow(self.left_subwin)

        # Right Subwindow (90%)
        right_widget = QTextEdit("Right Subwindow - 90%")
        self.right_subwin = QMdiSubWindow()
        self.right_subwin.setWidget(right_widget)
        self.right_subwin.setWindowTitle("Right Subwindow")
        self.right_subwin.resize(right_width, screen_height)
        self.mdi_area.addSubWindow(self.right_subwin)

        # Move windows to maintain 10:90 split
        self.left_subwin.move(0, 0)
        self.right_subwin.move(left_width, 0)

        self.left_subwin.show()
        self.right_subwin.show()

    def resizeEvent(self, event):
        """ Ensure the 10:90 split is maintained when resizing. """
        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()

        # Update the width of the left and right subwindows based on the main window's size
        left_width = int(screen_width * 0.1)
        right_width = int(screen_width * 0.9)

        # Resize the subwindows and move the right subwindow to maintain the 10:90 split
        self.left_subwin.resize(left_width, screen_height)
        self.right_subwin.resize(right_width, screen_height)
        self.right_subwin.move(left_width, 0)

        # Resize the sidebar widget inside the left subwindow
        self.sidebar.resize(left_width, screen_height)

        # Force the layout to update (important when resizing from a maximized window)
        self.sidebar.ui.verticalLayout.update()

        super().resizeEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth_dialog = AuthenticationSystem()
    if auth_dialog.exec() == QDialog.Accepted:
        sys.exit(app.exec())
