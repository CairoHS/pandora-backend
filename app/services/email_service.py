from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText


class EmailService():
    import smtplib


def send_email():
    # Configuração inicial

    # O SMTP(Simple Mail Transfer Protocol) É o Protocolo Usado Para Enviar E-mails Através Da Internet.
    smtp_server = "smtp.gmail.com"
    # Difine a Porta Que Será Usada Para a Comunicação Com o Servidor SMTP
    smtp_port = 587
    # Contém o Endereço de E-mail Que Será Usado para Envia A Mensagem
    email_sender = "faleconosco.pandoratec@gmail.com"
    # Use sua senha de aplicativo aqui
    email_password = "suasenhadeaplicativo"
    # Contém o Endereço  de E-mail De Quem Vai Receber.
    email_receiver = "destinatario@gmail.com"

    # Criando a mensagem
    # Permite Incluir Diferentes tipos de Conteúdo No E-mail.(texto ou Anexo)
    msg = MIMEMultipart()
    # Identifica Quem Está Enviando o E-mail
    msg['From'] = email_sender
    # Indica para Quem o E-mail Está Sendo Enviado.
    msg['To'] = email_receiver
    # Especifica o Assunto do E-mail.
    msg['Subject'] = "Boas Vindas!"

    # Corpo do email
    # A Messagem Que Deseja Manda para O Úsuario.
    body = "Olá, Bem Vindo A Plataforma Pandora!"
    # "Plain"=(Texto Puro), o que Significa Será Exibido Como Texto Simples.
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conectando ao servidor SMTP do Gmail
        server = smtplib.SMTP(smtp_server, smtp_port)
        # Iniciando a comunicação segura
        server.starttls()
        # Login no servidor
        server.login(email_sender, email_password)
        # Autentica o Remetente no  Servidor, Garantindo Permissão para Enviar E-mails Através Daquela Conta.
        server.sendmail(email_sender, email_receiver,
                        msg.as_stri())  # Enviando o e-mail
        server.quit()  # Finalizando a conexão

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar o e-mail: {str(e)}")


send_email()
