import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Qt
from views.py.ui_contacts_email import Ui_contacts_email

class ContactsEmail(QDialog):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "antonicokenquitayen@gmail.com"
    SENDER_PASSWORD = "awvj zjxc fita roxy"  # 🔹 Use App Password, NOT real password

    def __init__(self, contact_email_address, parent=None):
        super().__init__(parent)
        self.ui = Ui_contacts_email()
        self.ui.setupUi(self)

        # ✅ Prepopulate recipient email
        self.ui.recipient_line.setText(contact_email_address)

        # ✅ Keep window on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # ✅ Connect send button to the email function
        self.ui.send_btn.clicked.connect(self.send_email)

    def move_to_bottom_right(self):
        """Moves the dialog to the bottom-right of MainWindow."""
        if not self.parent():
            return

        main_rect = self.parent().geometry()
        self.move(
            main_rect.x() + main_rect.width() - self.width() - 40,
            main_rect.y() + main_rect.height() - self.height() - 95,
        )

    def send_email(self):
        """Handles SMTP email sending."""
        recipient = self.ui.recipient_line.text().strip()
        subject = self.ui.subject_line.text().strip()
        message = self.ui.email_txt.toPlainText().strip()

        if not recipient or not subject or not message:
            QMessageBox.warning(self, "Incomplete Fields", "Please fill all fields before sending.")
            return

        try:
            self._send_smtp_email(recipient, subject, message)
            QMessageBox.information(self, "Success", "Email sent successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send email.\n{str(e)}")

    def _send_smtp_email(self, recipient, subject, message):
        """Handles the SMTP connection and email sending."""
        print(f"Connecting to {self.SMTP_SERVER}:{self.SMTP_PORT} as {self.SENDER_EMAIL}")  # ✅ Debugging

        msg = MIMEMultipart()
        msg["From"] = self.SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
            server.ehlo()
            server.starttls()  # Secure connection
            server.ehlo()
            server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
            server.sendmail(self.SENDER_EMAIL, recipient, msg.as_string())
