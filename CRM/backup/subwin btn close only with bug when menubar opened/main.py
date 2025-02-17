import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QMdiArea, QMdiSubWindow, QMenuBar, QStatusBar, QWidget, QSizePolicy
from PySide6.QtCore import Qt

from ui_authenticationsystem import Ui_authenticationsystem
from ui_sidebar import Ui_sidebar
from ui_contacts import Ui_contacts

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

        # Add back2login button connection
        self.ui.back2login_button.clicked.connect(self.show_login)

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

        conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\CRM\mydb.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.open_mainwindow()
        else:
            self.passvalidation_label.setText("Username or password is incorrect")

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if self.stackedWidget.currentIndex() == 0:  # Login page
                self.login_button.click()
            elif self.stackedWidget.currentIndex() == 1:  # Signup page
                self.signup_button.click()
        else:
            super().keyPressEvent(event)

    def signup(self):
        username = self.username_input_2.text().strip()
        password = self.password_input_2.text().strip()
        confirm_password = self.confirmpass_input.text().strip()

        # Check one validation at a time
        if not username:
            self.validation_label.setText("Username field is required")
            return
        if not password:
            self.validation_label.setText("Password field is required")
            return
        if not confirm_password:
            self.validation_label.setText("Confirm password field is required")
            return
        if len(password) < 8:
            self.validation_label.setText("Password must be at least 8 characters")
            return
        if not any(c.islower() for c in password):
            self.validation_label.setText("Password must contain a lowercase letter")
            return
        if not any(c.isupper() for c in password):
            self.validation_label.setText("Password must contain an uppercase letter")
            return
        if not any(c.isdigit() for c in password):
            self.validation_label.setText("Password must contain a number")
            return
        if not any(c in '!@#$%^&*()' for c in password):
            self.validation_label.setText("Password must contain a symbol (!@#$%^&*())")
            return
        if password != confirm_password:
            self.validation_label.setText("Passwords do not match")
            return

        conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\CRM\mydb.db")
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

class ContactsForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRM")

        # Setup menu bar and status bar
        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))

        # Add menu and actions
        self.create_menu()

        # Set the MDI Area manually
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)


        # Create and add subwindows
        self.create_subwindows()

        # Show maximized by default
        self.showMaximized()

    def create_menu(self):
        """ Create menu bar with Open > Subwindow > Left, Right options. """
        open_menu = self.menuBar().addMenu("Open")
        subwindow_menu = open_menu.addMenu("Subwindow")

        left_action = subwindow_menu.addAction("Left")
        right_action = subwindow_menu.addAction("Right")

        left_action.triggered.connect(self.open_left_subwindow)
        right_action.triggered.connect(self.open_right_subwindow)

    def open_left_subwindow(self):
        """ Open the left subwindow with its contents. """
        if not self.left_subwin.isVisible():
            self.sidebar = SidebarForm()  # Ensure sidebar is initialized
            self.left_subwin.setWidget(self.sidebar)  # Set sidebar as widget
        self.left_subwin.setWindowTitle("")  # Set window title to empty
        self.left_subwin.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # Only show close button
        self.left_subwin.show()

    def open_right_subwindow(self):
        """ Open the right subwindow with the Contacts UI. """
        if not self.right_subwin.isVisible():
            self.contacts_widget = ContactsForm()  # Load contacts UI
            self.right_subwin.setWidget(self.contacts_widget)  # Set contacts as widget
        self.right_subwin.setWindowTitle("")  # Set window title to empty
        self.right_subwin.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # Only show close button
        self.right_subwin.show()

    def create_subwindows(self):
        """ Create two subwindows with a 10:90 split inside the MDI area. """
        screen_width = self.screen().availableGeometry().width()
        screen_height = self.screen().availableGeometry().height() - self.menuBar().height() - self.statusBar().height()

        left_width = int(screen_width * 0.1)
        right_width = int(screen_width * 0.9)

        # Left Sidebar
        self.sidebar = SidebarForm()
        self.left_subwin = QMdiSubWindow()
        self.left_subwin.setWidget(self.sidebar)
        self.left_subwin.setWindowTitle("")
        self.left_subwin.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # Only show close button
        self.left_subwin.resize(left_width, screen_height)
        self.left_subwin.setFixedWidth(left_width)  # Prevent manual resizing
        self.mdi_area.addSubWindow(self.left_subwin)

        # Right Contacts Window
        self.contacts_widget = ContactsForm()
        self.right_subwin = QMdiSubWindow()
        self.right_subwin.setWidget(self.contacts_widget)
        self.right_subwin.setWindowTitle("")
        self.right_subwin.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # Only show close button
        self.right_subwin.resize(right_width, screen_height)
        self.mdi_area.addSubWindow(self.right_subwin)

        self.left_subwin.move(0, 0)
        self.right_subwin.move(left_width, 0)

        self.left_subwin.show()
        self.right_subwin.show()


    def resizeEvent(self, event):
        """ Ensure the 10:90 split is maintained when resizing. """
        screen_width = self.width()
        screen_height = self.height() - self.menuBar().height() - self.statusBar().height()

        left_width = int(screen_width * 0.1)
        right_width = int(screen_width * 0.9)

        self.left_subwin.resize(left_width, screen_height)
        self.right_subwin.resize(right_width, screen_height)
        self.right_subwin.move(left_width, 0)

        self.sidebar.resize(left_width, screen_height)
        self.contacts_widget.resize(right_width, screen_height)  # Ensure contacts widget resizes

        self.sidebar.ui.verticalLayout.update()
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load and apply the QSS file
    try:
        with open("style.qss", "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print("⚠️ Warning: style.qss file not found!")

    #auth_dialog = AuthenticationSystem()
    #if auth_dialog.exec() == QDialog.Accepted:
    #    main_win = MainWindow()
    #    sys.exit(app.exec())

    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


