'''
Sistema de Figuras Geométricas
Objetivo: Practicar herencia y polimorfismo.
Descripción:
Crea una clase abstracta Figura con un método calcular_area que 
sea obligatorio implementar.
Implementa clases derivadas como Circulo, Rectangulo, y Triangulo.
Cada clase debe implementar el cálculo del área según su fórmula.
Crea una función que reciba una lista de figuras y calcule el área total.
'''

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = 3.1416 * self.radio ** 2
        return area

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
        
    
circulo = Circulo(5)
rectangulo = Rectangulo(9, 6)
triangulo = Triangulo(9, 3)

print(circulo.calcular_area()) 
print(rectangulo.calcular_area()) 
print(triangulo.calcular_area()) 

lista_figuras = [circulo, rectangulo, triangulo]

def area_total(lista_figuras):
    total = 0
    for figura in lista_figuras:
        total += figura.calcular_area()
    return total

print(area_total(lista_figuras))
        


