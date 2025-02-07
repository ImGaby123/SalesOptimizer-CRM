import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QIcon
from ui_contacts import Ui_contacts  # from (python you want to test) import (class of your pythonfile)

class MainWindow(QMainWindow, Ui_contacts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set the initial page of stackedWidget to 0
        self.stackedWidget.setCurrentIndex(0)

        # Create an action for the UploadPic QLineEdit
        self.add_upload_pic_action()

    def add_upload_pic_action(self):
        # Create a QIcon for the image you want to use
        icon = QIcon(":/new/newPrefix/Resources/upload.png")

        # Create an action and add the icon to the leading position of UploadPic QLineEdit
        action = self.UploadPic.addAction(icon, QLineEdit.LeadingPosition)

        # Optionally, you can make the action clickable and perform a function when clicked
        action.triggered.connect(self.upload_pic_clicked)

    def upload_pic_clicked(self):
        # You can implement any function you want when the action is clicked
        print("Upload picture action clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
