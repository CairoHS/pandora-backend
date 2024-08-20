class EmailService():
    def email(validar_email):
        import re


# Definindo o Regex Para Validar o E-mail
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def validar(email):
    if re.fullmatch(regex, email):  # type: ignore
        print("Email Válido")
    else:
        print("Email Inválido")
