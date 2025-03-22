import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PySide6.QtWidgets import QDialog, QMessageBox
from views.py.ui_contacts_email import Ui_contacts_email

class ContactsEmail(QDialog):
    def __init__(self, contact_email_address):
        super().__init__()
        self.ui = Ui_contacts_email()
        self.ui.setupUi(self)

        # ✅ Pre-fill recipient
        self.ui.recipient_line.setText(contact_email_address)

        # ✅ Connect send button
        self.ui.send_btn.clicked.connect(self.send_email)

    def send_email(self):
        """Handles SMTP email sending."""
        sender_email = "antonicokenquitayen@gmail.com"
        sender_password = "awvj zjxc fita roxy"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        recipient = self.ui.recipient_line.text().strip()
        subject = self.ui.subject_line.text().strip()
        message = self.ui.email_txt.toPlainText().strip()

        if not recipient or not subject or not message:
            QMessageBox.warning(self, "Incomplete Fields", "Please fill all fields before sending.")
            return

        try:
            # ✅ Setup email structure
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # ✅ Connect to SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
            server.quit()

            QMessageBox.information(self, "Success", "Email sent successfully!")

            # ✅ Close the dialog on success
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send email.\n{str(e)}")
