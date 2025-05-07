import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QProgressBar, QLabel, QMessageBox
)
from PySide6.QtCore import QTimer, Qt

from models.LeadScoring import LeadScoring as LS
from Data.Lead_Data import Lead_Data
from DB.db_functions import db_functions
from DB.db_connection import db_connection

class LoadLeadScore(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Updating Lead Scores")
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setGeometry(100, 100, 400, 120)

        self.layout = QVBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMaximum(100)
        self.label = QLabel("Please Do Not Shutdown!")
        self.label.setAlignment(Qt.AlignCenter)

        self.title = QLabel("-")
        self.title.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.title)
        self.setLayout(self.layout)

        # Setup
        self.db = db_functions(db_connection())
        self.scorer = LS()
        self.data = Lead_Data()
        self.leads = self.data.getLeadInformation()
        self.total = len(self.leads)
        self.index = 0

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_lead)
        self.timer.start(10)  # speed can be adjusted

    def process_lead(self):
        if self.index < self.total:
            lead = self.leads[self.index]

            # Assign Specific Data
            ID = str(lead[0]).upper()
            Country = lead[1].upper()
            City = lead[2].upper()
            JobTitle = lead[3].upper()
            Industry = lead[4].upper()
            yrsInIndustry = lead[5]

            # Update Title Label
            self.title.setText(f"Updating Lead ID: {ID}")

            # 1. Assign Lead Instance
            instance = {1: Country, 2: City, 3: JobTitle, 4: Industry, 5: yrsInIndustry}
            
            # 2. Convert Each Attribute to its corresponding score
            converted = self.scorer.lead_Score_Assignment(instance)
            
             # 3. Compute the Converted Value
            score = self.scorer.lead_Score_Computation(converted)

            # 4. Save to database
            self.db.update_leadScores(lead[0], score)

            self.index += 1
            percent = int((self.index / self.total) * 100)
            self.progress_bar.setValue(percent)
        else:
            self.timer.stop()
            QMessageBox.information(self, "Done", "Lead scores updated successfully!")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadLeadScore()
    window.show()
    sys.exit(app.exec())
