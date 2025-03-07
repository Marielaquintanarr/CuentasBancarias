# Encapsulamiento: protege los elementos de una clase
# No existe en python
# Privado - no puede acceder ni el desarrollar

# En python si existen pero al final todos son publicos


class MiClass:
    def __init__(self):
        # al usar _ indica a python que el atributo es privado
        #self._atributo_privado = 'valor'
        # atributos muy privados con doble __, sale error (pero si se podria acceder)
        self.__atributo_privado = 'valor'
    # metodo privado
    def __hablar(self):
        print('Holaaa')

objeto = MiClass()
print(objeto.__atributo_privado)

objeto.__hablar()

# protegido que solo se pueda acceder de sus clases o subclases
# Nos ayuda a proteger atributos, mejora la legibildad del codigo, la evolucion y codigo
# Para acceder a un dato que esta encapsulado se usan geters y seters
# getter -> metodo para acceder a un atributo 
# setter -> modificar / establecer el valor de un atributo