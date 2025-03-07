# metodos que se llaman igual pero que hace distintas cosas

class Gato:
    def hablar(self):
        print('Miau')


class Perro:
    def hablar(self):
        print('Woof')

gato = Gato()
perro = Perro()

gato.hablar()
perro.hablar()


def hacer_sonido(animal):
    animal.hablar()

hacer_sonido(perro)

# en los lenguajes de tipo dinamico no se necesita hacer herencia para tener polimorfismo

