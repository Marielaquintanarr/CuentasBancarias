# abstraccion -> manejar la complejidad, quitando complicaciones para el usuario
# solo le dan lo indispensable
# no tienes que saber como funciona si no como usarlo

class Auto:
    def __init__(self):
        self.__estado = 'apagado'

    def encender(self):
        self.__estado = 'encendido'
        print('el auto esta encendido')
    
    def conducir(self):
        if self.__estado == 'apagado':
            self.encender()
        print('conduciendo')


mi_auto = Auto()
mi_auto.conducir()