# porperty nos indica que hay un getter o un setter, y en get_nombre ya no se usa get_nombre()
# todo esto para que el desarrollador no pueda acceder a _nombre
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    
    # deleter
    @nombre.deleter
    def nombre(self):
        del self._nombre

mariela = Persona('mariela', 20)

nombre = mariela.nombre
print(nombre)

mariela.nombre = 'PEPE'

nombre = mariela.nombre
print(nombre)

del mariela.nombre

nombre = mariela.nombre
print(nombre)