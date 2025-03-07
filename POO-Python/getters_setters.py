# getter -> obtener
# setter -> establecer / modificar valor

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, value):
        self.__nombre = value



dalto = Persona('Mariela', '21')

dalto.set_nombre('Jaime')
nombre = dalto.get_nombre()
print(nombre)