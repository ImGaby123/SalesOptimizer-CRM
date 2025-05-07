import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PySide6.QtCore import QTimer

class LeadProgressBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lead Progress")
        self.setGeometry(100, 100, 300, 100)

        self.total_leads = 250
        self.current_lead = 0

        self.layout = QVBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)  # Progress bar scale is still 0–100
        self.progress_bar.setValue(0)

        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(20)  # Speed up for demo

    def update_progress(self):
        if self.current_lead < self.total_leads:
            self.current_lead += 1
            percent = (self.current_lead / self.total_leads) * 100
            self.progress_bar.setValue(int(percent))
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LeadProgressBar()
    window.show()
    sys.exit(app.exec_())
