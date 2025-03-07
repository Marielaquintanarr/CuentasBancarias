'''
10. Sistema de Notificaciones
Objetivo: Practicar polimorfismo.
Descripción:
Diseña una clase base Notificacion con un método abstracto enviar.
Implementa clases concretas como NotificacionEmail, NotificacionSMS, y NotificacionPush.
Crea un sistema que permita enviar notificaciones a diferentes usuarios dependiendo del tipo.
'''
from abc import ABC, abstractmethod
class Notificacion:
    def __init__(self, contenido):
        self.contenido = contenido
        
    @abstractmethod
    def enviar(self):
        pass

class Usuario:
    def __init__(self, nombre, ):
        pass
class NotificacionEmail(Notificacion):
    def __init__(self, contenido, sender, email):
        super().__init__(contenido)
        self.sender = sender
        self.email = email