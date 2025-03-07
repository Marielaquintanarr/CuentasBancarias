# # Heredencia

# class Galleta():
#     def __init__(self, nombre, sabor, tamaño, relleno):
#         self.nombre = nombre
#         self.sabor = sabor
#         self.tamaño = tamaño
#         self.relleno = relleno

# # pass - cuando queremos crear algo pero no queremos definir que es
# class GalletaAvena(Galleta):
#     def __init__(self, nombre, sabor, tamaño, relleno, gluten, cantidad_avena):
#         super().__init__(nombre, sabor, tamaño, relleno)
#         self.gluten = gluten
#         self.cantidad_avena = cantidad_avena

# galleta1 = GalletaAvena('Galleta de chispas', 'Vanilla', 'Chica', 'Nutella', 20, '50%')


# print(galleta1.cantidad_avena)


# Herencia multiple

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('hola')


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad}')
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario):
        super().__init__(nombre, edad, nacionalidad)      
        self.salario = salario

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # se heredan las dos clases con el Clase.__init___
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    # Para heredar metodos
    def presentarse(self):
        # se usa super().metodo, tambien se puede usar self.metodo, con super
        # siempre se regresa la funcion, aun si pongo otro print
        # en las funciones hijas no cambia
        return f'{super().mostrar_habilidad()}'
    

p1 = EmpleadoArtista('Mariela', '19', 'Mexicana', 'Bailar', '200,000', 'Datadog')

# para ver si una clase esta heredada de otra
# issubclass(es una subclase, de esta clase?)
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)

# saber instancia
instancia = isinstance(p1, EmpleadoArtista)
instancia = isinstance(p1, Artista)
print(instancia)

# si en dos clases tuviera un atributo o funcion con el mismo nombre que otra
# se usa el MRO (Method Resolution Order) -> segun el orden que se corra primero