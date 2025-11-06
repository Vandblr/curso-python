from dotenv import load_dotenv
from os import getenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


load_dotenv()

def __obter_login() -> str:
    email = getenv("EMAIL")
    if email is None:
        raise Exception("Login não está preenchido no arquivo .env")

    return email


def __obter_senha() -> str:
    senha = getenv("SENHA")
    if senha is None:
        raise Exception("Senha não está preenchida no arquivo .env")
    return senha

def enviar(destinatario: str, corpo: str):
    mensagem = MINEmultipart()
    mensagem["from"] = __obter_login()
    mensagem["TO"] = destinatario
    mensagem["Subject"] = "Pedido criado"
    mensagem.attach(MIMEtext(corpo, "Plain"))

    try:
       with smtplib.SMTP("sntp.gmail.com", 587) as servidor:
          servidor.starttls() #criptografia da conexão
          servidor.login(__obter_login(), __obter_senha())
          servidor.send.mensagem(mensagem)
          print("E-mail enviado com sucesso")
    except Exception as e:
      print("erro ao enviar e-mail:", e)

def enviar_email_pedido(destinatario: str, tamanho: str, sabores: list[str]):
   mensagem = f"""Pedido criao com sucesso!

   Tamanho da pizza: {tamanho}
   Sabores: {",".join(sabores)}
   """

   enviar(destinatario, mensagem)


