# metodos especiales (dunder) -> __init__ es un metodo especial, empiezan con __ y terminan con __
# __str__ a un objeto le muestra como mostrarse en pantalla

class Lista:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Lista({self.nombre}, {self.edad})'
    
    # reconstruir el objeto
    def __repr__(self):
        return f'Lista("{self.nombre}", {self.edad})'
    
    # sumar objetos
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Lista(self.nombre + ' ' + otro.nombre, nuevo_valor)
    
mariela = Lista('Mariela', 20)
pepe = Lista('Pepe', 26)

repre = repr(mariela)
resultado = eval(repre)

r = mariela + pepe 
print(r.edad)
print(r.nombre)