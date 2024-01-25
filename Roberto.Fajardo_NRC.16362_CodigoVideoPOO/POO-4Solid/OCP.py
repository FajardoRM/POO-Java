class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario['email']}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario['SMS']}")

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando WhatsApp a {self.usuario['whatsapp']}")

class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando Twitter a {self.usuario['twitter']}")

# Crear un usuario de ejemplo
usuario_ejemplo = {
    'email': 'usuario@example.com',
    'SMS': '123456789',
    'whatsapp': '987654321',
    'twitter': '@usuario_twitter'
}

# Crear instancias de las clases 
notif_email = NotificadorEmail(usuario_ejemplo, "¡Hola por email!")
notif_sms = NotificadorSMS(usuario_ejemplo, "¡Hola por SMS!")
notif_whatsapp = NotificadorWhatsApp(usuario_ejemplo, "¡Hola por WhatsApp!")
notif_twitter = NotificadorTwitter(usuario_ejemplo, "¡Hola por Twitter!")

# Llamar al método
notif_email.notificar()
notif_sms.notificar()
notif_whatsapp.notificar()
notif_twitter.notificar()

      