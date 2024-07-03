import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('APP_PASSWORD')
name_database = os.getenv('NAME_DATABASE')
smtp = os.getenv('SMTP')
smtp_port = os.getenv('SMTP_PORT')
