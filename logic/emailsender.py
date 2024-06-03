from email.message import EmailMessage
import smtplib

class send_email:
    def __init__(self, sender: str, recipients: list, password: str, message:str, subject ) ->None:
        self.sender = sender
        self.recipients = recipients
        self.password = password
        self.message = message
        self.subject = subject
        
        
    def send(self):
        # Crear el mensaje
        message = EmailMessage()
        message["From"] = self.sender
        message["To"] = self.recipients
        message["Subject"] = self.subject
        message.set_content(f"{self.message}")
        
        # Configuración del servidor SMTP
        smtp_server = "smtp-mail.outlook.com"
        port = 587
        
        # Enviar el correo
        try:
          with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Asegurar la conexión
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.recipients, message.as_string())
        except:
          return('Ocurrio un error durante el envio de los correos por favor intentelo de nuevo.')
        
            
        return "Correos enviados exitosamente!"