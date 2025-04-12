from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from views.py.ui_add_opportunity import Ui_add_opportunity

class AddOpportunity(QDialog):
    def __init__(self, contact_id=None, parent=None):
        super().__init__(parent)
        self.contact_id = contact_id
        self.ui = Ui_add_opportunity()
        self.ui.setupUi(self)

        # Window Settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Needed for rounded corners if using stylesheet
        self.setWindowFlags(self.windowFlags() | self.windowFlags() | self.windowFlags().WindowStaysOnTopHint)

        #Make dialog draggable since there's no windows
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.drag_position = event.globalPosition().toPoint()
                event.accept()

        #Stylesheet
        self.ui.main_frame.setStyleSheet("""
            background-color: #171717;
            border-radius: 10px;
        """)

        self.ui.cancel_btn.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_position)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

