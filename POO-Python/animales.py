'''
6. Gestión de Animales
Objetivo: Practicar polimorfismo.
Descripción:
Crea una clase base Animal con un método abstracto
 hacer_sonido.
Implementa clases como Perro, Gato, y Pajaro, 
donde cada una sobrescriba el método con su sonido 
característico.
Implementa una función que reciba una lista de 
animales y haga que cada uno produzca su sonido.
'''

from abc import abstractmethod, ABC

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print('Woof')

class Gato(Animal):
    def hacer_sonido(self):
        print('Miau')

class Pajaro(Animal):
    def hacer_sonido(self):
        print('Pio Pio')


perro = Perro()
gato = Gato()
pajaro = Pajaro()

lista_animales = [perro, gato, pajaro]

def sonidos(lista_animales):
    for animal in lista_animales:
        animal.hacer_sonido()

sonidos(lista_animales)


