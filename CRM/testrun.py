import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_contacts import Ui_contacts  # from (python you want to test) import (class of your pythonfile)

class MainWindow(QMainWindow, Ui_contacts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
