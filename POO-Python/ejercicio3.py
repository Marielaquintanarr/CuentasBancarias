class Animal:
    def comer(self):
        print('Como')


class Mamifero(Animal):
    def amamantar(self):
        print('Amamanto')


class Ave(Animal):
    def volar(self):
        print('Vuelo')


class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.amamantar()
murcielago.comer()
murcielago.volar()


