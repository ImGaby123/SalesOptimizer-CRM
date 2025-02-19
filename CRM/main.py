import sys
from PySide6.QtWidgets import QApplication
from models.models_authentication import AuthenticationSystem

app = QApplication(sys.argv)
window = AuthenticationSystem()  # Siguraduhin na ito ay subclass ng QMainWindow
window.show()
app.exec()
