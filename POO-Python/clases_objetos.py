# # Crear clase
# # snake case con_guiones
# # camel case conGuiones
# # pascal case ConGuiones -> se usa para clases


# class Celular():
#     # atributos estaticos
#     marca = 'Iphone'
#     modelo = '15 pro max'
#     camara = '48MP'


# # Un objeto es la instancia de una clase. Puedo crear varios celulares porque ya tengo la clase

# celular1 = Celular()
# print(celular1.marca)

# self es para hacer una referencia a si mismo
# es como celular1.marca = self.marca
class Celular():
    def __init__(self, marca, modelo, camara):
        # cada self es una propiedad de self
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # metodos
    # se les tiene que pasar el self para que el objeto pueda acceder a ellos
    def llamar(self):
        print(f'Estas haciendo una llamada desde un {self.modelo}')

    def colgar(self):
        print('Colgaste')


# self.marca -> propiedad
# marca = 'apple'

celular1 = Celular('Apple', 'iPhone 15 pro', '15MP')
celular2 = Celular('Samsung', 'S23', '48MP')
celular1.llamar()




