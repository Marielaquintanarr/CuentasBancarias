# clases, modulos y funciones tienen que estar abiertas para extension y cerradas para modificacion

class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    
    def notificar(self):
        raise NotImplementedError
        
class NotificadorEmail(Notificacion):
    def Notificar(self):
        print(f'Enviando mensaje por mail a {self.usuario.email}')

class NotificadorSMS(Notificacion):
    def Notificar(self):
        print(f'Enviando mensaje por SMS a {self.usuario.sms}')


class NotificadorWhatsapp(Notificacion):
    def Notificar(self):
        print(f'Enviando mensaje por Whatsapp a {self.usuario.whatsapp}')