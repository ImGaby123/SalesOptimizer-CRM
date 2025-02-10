import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QLabel, QHeaderView, QLineEdit
from ui_contacts import Ui_contacts  # Your UI file

class MainWindow(QMainWindow, Ui_contacts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
