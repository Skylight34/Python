from pyteams import connectorcard

# Lista de correos electrónicos de los destinatarios
emails = ['angel.trasfi@uberfreight.com']  # Agrega los correos deseados

# Mensaje a enviar
message = "¡Hola! Este es un mensaje enviado desde Python a través de Microsoft Teams."

# Crear una instancia de ConnectorCard
card = connectorcard.ConnectorCard()

# Configurar el mensaje y los destinatarios
card.text(message)
for email in emails:
    card.add_email(email)

# Enviar el mensaje
webhook_url = 'URL_DEL_WEBHOOK_DE_TEAMS'  # Reemplaza con tu URL de Webhook de Teams
card.send(webhook_url)
