# Bot de Envío de Correos Máximos 

Este proyecto es un script en Python que permite enviar correos electrónicos automáticamente usando `smtplib` y `email.message`.

##  Tecnologías utilizadas

- Python 
- smtplib
- email.message

##  Cómo usar

1. Clona el repositorio o copia este proyecto.
2. Abre el archivo `enviar_correos.py`.
3. Edita las siguientes variables con tus datos:

```python
EMAIL_SENDER = "tu_correo@gmail.com"
EMAIL_PASSWORD = "contraseña_de_aplicacion_generada"
EMAIL_RECEIVER = "destinatario@gmail.com"




##  Configuración para cuentas de Gmail

Si vas a utilizar una cuenta de Gmail como remitente (EMAIL_SENDER), tené en cuenta lo siguiente:

1. Activá la verificación en dos pasos en tu cuenta de Gmail.  
   Podés hacerlo desde: [https://myaccount.google.com/security]

2. Generá una "Contraseña de aplicación"** desde la configuración de seguridad de tu cuenta.

   - Iniciá sesión en tu cuenta de Gmail.
   - Andá a "Seguridad" > "Contraseñas de aplicaciones".
   - Seleccioná "Correo" como app y "Dispositivo personalizado".
   - Te dará una contraseña de 16 caracteres que vas a usar en lugar de tu contraseña real en el script.

3. Usá esa contraseña en tu variable (EMAIL_PASSWORD) 

   
   


