import smtplib
from email.message import EmailMessage
from settings_env import smtp, smtp_port, email, password


class EmailSender:
    """
    Класс для отправки электронных писем.
    """

    def __init__(self, recipient, subject, text_message):
        self.my_email = email
        self.server = smtplib.SMTP(smtp, smtp_port)
        self.server.starttls()
        self.server.login(email, password)
        self.email = EmailMessage()
        self.recipient = recipient
        self.subject = subject
        self.text_message = text_message

    def send_message(self):
        """
        Отправляет электронное письмо
        """
        self.email['From'] = self.my_email
        self.email['To'] = self.recipient
        self.email['Subject'] = self.subject
        self.email.set_content(self.text_message)
        self.server.send_message(self.email)
