import sys
import os
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from models.models_authentication import MainWindow

# Initialize the application
app = QApplication(sys.argv)

# ✅ Use QRC path directly if you're using a .qrc file compiled with pyrcc or qrc in QtCreator
app.setWindowIcon(QIcon(":/Resources/crm_blck.png"))

# Load and apply QSS stylesheet
qss_file = "views/qss/style.qss"

if not os.path.exists(qss_file):
    error_msg = f"QSS file '{qss_file}' not found. The application will run without styles."
    QMessageBox.warning(None, "Missing Stylesheet", error_msg)
else:
    with open(qss_file, "r") as file:
        app.setStyleSheet(file.read())

# Create and show the main window
try:
    window = MainWindow()
    window.show()
except Exception as e:
    QMessageBox.critical(None, "Application Error", f"Failed to start application:\n{e}")
    sys.exit(1)

sys.exit(app.exec())
