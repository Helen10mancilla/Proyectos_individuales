import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  

#  Configuración del servidor SMTP de Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
#correo del remitente
EMAIL_SENDER = "tu_correo@gmail.com" 
#contraseña del remitente
EMAIL_PASSWORD = "contraseña_de_aplicacion_generada"

#  Función para enviar correo
def enviar_correo(destinatario, asunto, mensaje):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg["Subject"] = asunto

    msg.attach(MIMEText(mensaje, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Seguridad
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, destinatario, msg.as_string())
        server.quit()
        print(f" Correo enviado a {destinatario}")
    except Exception as e:
        print(f" Error al enviar correo: {e}")

#  Prueba del bot
destinatario = "destinatario@gmail.com" #correo del destinatario
asunto = "" 
mensaje = ""

enviar_correo(destinatario, asunto, mensaje)
