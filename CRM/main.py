import sys
import os
import sqlite3
from PySide6.QtWidgets import (QApplication, QDialog, QMessageBox, QMainWindow, QMdiArea, QMdiSubWindow, QWidget,
                               QMenuBar, QStatusBar, QSizePolicy)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from views.py.ui_authenticationsystem import Ui_authenticationsystem
from views.py.ui_sidebar import Ui_sidebar
from views.py.ui_contacts import Ui_contacts


# Get the current directory (where the script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the relative path to the database
db_path = os.path.join(current_dir, 'datas', 'mydb.db')

# Connect to the SQLite database using the relative path
conn = sqlite3.connect(db_path)

class AuthenticationSystem(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_authenticationsystem()
        self.ui.setupUi(self)

        self.stackedWidget = self.ui.stackedWidget
        self.stackedWidget.setCurrentIndex(0)

        self.ui.login_button.clicked.connect(self.login)
        self.ui.createacc_button.clicked.connect(lambda: self.switch_page(1))
        self.ui.signup_button.clicked.connect(self.signup)
        self.ui.back2login_button.clicked.connect(lambda: self.switch_page(0))

        # Dynamic password validation
        self.ui.password_input_2.textChanged.connect(self.validate_password)

        self.show()

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def login(self):
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()

        if not username:
            self.ui.uservalidation_label.setText("Username field is required")
            return
        if not password:
            self.ui.passvalidation_label.setText("Password field is required")
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts_tbl WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.open_mainwindow()
        else:
            self.ui.passvalidation_label.setText("Username or password is incorrect")

    def validate_password(self):
        """ Dynamically validate password strength and update the message. """
        password = self.ui.password_input_2.text().strip()
        messages = []

        if len(password) < 8:
            messages.append("🔴 Must be at least 8 characters.")
        else:
            messages.append("✅ At least 8 characters.")

        if not any(c.islower() for c in password):
            messages.append("🔴 Must contain a lowercase letter.")
        else:
            messages.append("✅ Contains a lowercase letter.")

        if not any(c.isupper() for c in password):
            messages.append("🔴 Must contain an uppercase letter.")
        else:
            messages.append("✅ Contains an uppercase letter.")

        # Number or symbol validation combined
        if not any(c.isdigit() for c in password) and not any(c in '!@#$%^&*()' for c in password):
            messages.append("🔴 Must contain a number or a symbol (!@#$%^&*()).")
        else:
            messages.append("✅ Contains a number or a symbol.")

        self.ui.validation_label.setText("\n".join(messages))

    def signup(self):
        """ Handles user signup with final password validation. """
        username = self.ui.username_input_2.text().strip()
        password = self.ui.password_input_2.text().strip()
        confirm_password = self.ui.confirmpass_input.text().strip()

        if not username:
            self.ui.validation_label.setText("Username field is required")
            return
        if not password:
            self.ui.validation_label.setText("Password field is required")
            return
        if not confirm_password:
            self.ui.validation_label.setText("Confirm password field is required")
            return
        if password != confirm_password:
            self.ui.validation_label.setText("Passwords do not match")
            return

        # Final validation before saving
        validation_text = self.ui.validation_label.text()
        if "🔴" in validation_text:
            QMessageBox.warning(self, "Invalid Password", "Please meet all password requirements before signing up.")
            return

        conn = sqlite3.connect(db_path)
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
        
        self.setMenuBar(QMenuBar(self))
        self.setStatusBar(QStatusBar(self))
        
        self.transposed = False  # Track the state of transposition
        self.sidebar_visible = True  # Track sidebar visibility
        
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
        
        self.left_subwin = self.create_mdi_subwindow(SidebarForm(), int(screen_width * 0.1), screen_height, 0, 0)
        self.right_subwin = self.create_mdi_subwindow(MainForm(), int(screen_width * 0.9), screen_height, int(screen_width * 0.1), 0)
        
        self.left_subwin.closeEvent = self.handle_left_close

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
        self.transposed = not self.transposed  # Toggle transposition state
        self.left_subwin, self.right_subwin = self.right_subwin, self.left_subwin
        self.realign_subwindows()
    
    def toggle_sidebar(self):
        self.sidebar_visible = not self.sidebar_visible
        self.left_subwin.setVisible(self.sidebar_visible)
        self.sidebar_action.setChecked(self.sidebar_visible)
        self.realign_subwindows()
    
    def toggle_mainform(self):
        self.right_subwin.setVisible(not self.right_subwin.isVisible())
        self.mainform_action.setChecked(self.right_subwin.isVisible())
    
    def handle_left_close(self, event):
        self.sidebar_visible = False
        self.left_subwin.setVisible(False)
        self.sidebar_action.setChecked(False)
        self.realign_subwindows()
        event.accept()
    
    def resizeEvent(self, event):
        self.realign_subwindows()
        super().resizeEvent(event)

class SidebarForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sidebar()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(self.ui.verticalLayout)

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_contacts()
        self.ui.setupUi(self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("views/qss/style.qss", "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print("⚠️ Warning: style.qss file not found!")

    #main_win = MainWindow()
    main_win = AuthenticationSystem()
    main_win.show()
    sys.exit(app.exec())
