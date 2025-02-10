import sys
<<<<<<< HEAD
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QLabel, QHeaderView, QLineEdit
from ui_contacts import Ui_contacts  # Your UI file
=======
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QIcon
from ui_contacts import Ui_contacts  # from (python you want to test) import (class of your pythonfile)
>>>>>>> f3607c82b554142f74c1aa5daa949368535c9388

class MainWindow(QMainWindow, Ui_contacts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

<<<<<<< HEAD
        # Initialize current index for stacked widget
        self.current_page_index = 1

        # Connect navigation buttons
        self.btn_next = QPushButton("Next", self)
        self.btn_previous = QPushButton("Previous", self)

        # Set button positions (you can modify these as needed)
        self.btn_next.setGeometry(1100, 630, 80, 30)
        self.btn_previous.setGeometry(1000, 630, 80, 30)

        # Connect buttons to functions
        self.btn_next.clicked.connect(self.go_to_next_page)
        self.btn_previous.clicked.connect(self.go_to_previous_page)

        # Set initial page in stacked widget
        self.stackedWidget.setCurrentIndex(self.current_page_index)

        # Ensure QTableWidget columns stretch to fill the entire table
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def go_to_next_page(self):
        # Get the total number of pages in the stacked widget
        total_pages = self.stackedWidget.count()

        # Move to next page and wrap around
        self.current_page_index = (self.current_page_index + 1) % total_pages
        self.stackedWidget.setCurrentIndex(self.current_page_index)

    def go_to_previous_page(self):
        # Get the total number of pages in the stacked widget
        total_pages = self.stackedWidget.count()

        # Move to previous page and wrap around
        self.current_page_index = (self.current_page_index - 1) % total_pages
        self.stackedWidget.setCurrentIndex(self.current_page_index)
=======
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
>>>>>>> f3607c82b554142f74c1aa5daa949368535c9388

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
