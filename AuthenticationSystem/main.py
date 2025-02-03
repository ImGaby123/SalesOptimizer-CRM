import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QWidget, QMenu
from PySide6.QtGui import QAction
from ui_login import Ui_LoginDialog
from ui_signup import Ui_SignupDialog
from ui_sidebar import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
