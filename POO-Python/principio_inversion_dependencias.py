# # Los modulos de alto nivel no tienen que depender de los modulos de bajo nivel
# # no tenemos que depender de implementaciones especificas


# class Diccionario:
#     def verificar_palabras(self, palabra):
#         # logica
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
#         #usamos el diccionario para crear un diccionario
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografia:
    @abstractmethod
    def verificar_palabra(self, palabra):
        #logica
        pass


class Diccionario(VerificadorOrtografia):
    def verificar_palabra(self, palabra):
        # logica
        pass

class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self,texto):
        # usar verificador para checar el texto
        pass

class ServicioOnline(VerificadorOrtografia):
    def verificar_palabra(self, palabra):
        # logica para verificar palabras desde web
        pass

corrector = CorrectorOrtografico(Diccionario())
corrector.corregir_texto('hola')