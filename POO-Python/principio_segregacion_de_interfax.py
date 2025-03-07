# establece que ningun cliente debe ser forzado a utilizar interfaces que no utiliza

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        print('Estoy comiendo')


class Dormilon(ABC):
    @abstractmethod
    def dormir(self):
        print('Estoy durmiendo') 



class TrabajadorHumano(Trabajador, Comedor, Dormilon):
    def comer(self):
        print('El humano esta comiendo') 

    def trabajar(self):
        print('El humano esta trabajando') 

    def dormir(self):
        print('El humano esta durmiendo') 

class TrabajadorRobot(Trabajador):
    def trabajar(self):
        print('El robot esta trabajando')

# esto no va a funcionar porque me hacen falta comer y dormir
# como se soluciona esto? se divide la interfaz en interfaces mas pequeñas
robot = TrabajadorRobot()
humano = TrabajadorHumano()

humano.comer()