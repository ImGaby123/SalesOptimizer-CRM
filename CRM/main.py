import sys
import os
from PySide6.QtWidgets import QApplication, QMessageBox
from models.models_authentication import MainWindow

# Initialize the application
app = QApplication(sys.argv)

# Load and apply QSS stylesheet
qss_file = "views/qss/style.qss"

if not os.path.exists(qss_file):
    error_msg = f"QSS file '{qss_file}' not found. The application will run without styles."
    QMessageBox.warning(None, "Missing Stylesheet", error_msg)  # Visible alert for the user
else:
    with open(qss_file, "r") as file:
        app.setStyleSheet(file.read())

# Create and show the main window
try:
    window = MainWindow()  # Ensure this is a subclass of QMainWindow
    window.show()
except Exception as e:
    QMessageBox.critical(None, "Application Error", f"Failed to start application:\n{e}")
    sys.exit(1)  # Exit if the main window fails

# Run the application event loop
sys.exit(app.exec())
