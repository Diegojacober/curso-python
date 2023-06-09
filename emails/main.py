import os
from pathlib import Path
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

#Caminho arquivo html
PATH_HTML = Path(__file__).parent / 'email.html'

# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = 'diegoalencar.jacober@gmail.com'

# Configurações SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = os.getenv('SMTP_PORT', 587)
smtp_user = os.getenv('FROM_EMAIL', '')
smt_pass = os.getenv('EMAIL_PASSWORD', '')

#Fazer aula 183
with open(PATH_HTML, 'r', encoding='utf-8') as file:
    texto_arquivo = file.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Roberto')
    

#Tranformar a mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Testando Python'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smt_pass)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')