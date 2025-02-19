import sys
import os
from PySide6.QtWidgets import QApplication
#from models.models_authentication import AuthenticationSystem
from models.models_authentication import MainWindow

# Initialize the application
app = QApplication(sys.argv)

# Load and apply QSS stylesheet
qss_file = "views/qss/style.qss"

if os.path.exists(qss_file):
    with open(qss_file, "r") as file:
        app.setStyleSheet(file.read())
else:
    print(f"Warning: QSS file '{qss_file}' not found. The application will run without styles.")

# Create and show the main window
window = MainWindow()  # Ensure this is a subclass of QMainWindow
window.show()

# Run the application event loop
app.exec()
