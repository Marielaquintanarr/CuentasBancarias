# clases_abstractas -> es una clase que no podemos instanciar, es como una una plantilla para que podamos clases a apartir de ella
# como crear una clase persona, y creo clases estudiantes, empleados 

from abc import ABC, abstractclassmethod

# abstractclassmethod -> decorador
# abc 

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    # es un metodo abstracto porque todos tienen trabajos diferentes 
    def hacer_actividad(self):
        pass

    def presentarme(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} años')


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 
    
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad) 
    
    def hacer_actividad(self):
        print(f'Estoy trabajando en el rubro de: {self.actividad}')


dalto = Estudiante('Mariela', 20, 'Femeninimo', 'Programacion')
dalto.hacer_actividad()

pepe = Trabajador('Pepe', 29, 'Masculino', 'Programacion')
pepe.hacer_actividad()