'''
5. Sistema de Vehículos
Objetivo: Practicar herencia y polimorfismo.
Descripción:
Define una clase base Vehiculo con atributos como marca, modelo, y un método abstracto moverse.
Crea clases derivadas como Carro, Bicicleta, y Avion que implementen el método moverse de maneras diferentes.
Crea una función que recorra una lista de vehículos y los haga "moverse".
'''
from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def moverse(self):
        pass


class Carro(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad
    
    def moverse(self):
        print('El carro se esta moviendo')

class Avion(Vehiculo):
    def __init__(self, marca, modelo, tamaño):
        super().__init__(marca, modelo)
        self.tamaño = tamaño
    
    def moverse(self):
        print('El avion esta volando')

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def moverse(self):
        print('La bicicleta esta rodando')



carro1 = Carro('Kia', 'K4', '20L')
avion1 = Avion('Aeromexico', 'M-14', 'Jet Privado')
bicicleta1 = Bicicleta('Bento', 'Rapid-4', 'Montaña')

carro1.moverse()