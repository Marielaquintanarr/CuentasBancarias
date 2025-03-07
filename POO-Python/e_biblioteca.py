'''
Objetivo: Practicar encapsulación y abstracción.
Descripción:
Crea una clase Libro con atributos privados como titulo, autor, y disponible.
Implementa métodos para prestar y devolver libros.
Crea una clase Biblioteca que gestione un conjunto de 
libros y permita consultar su disponibilidad.
'''

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.disponible = True

    def prestar_libro(self):
        if self.disponible == True:
            self.disponible = False
            return 'El libro ha sido prestado'
        else:
            return 'El libro no esta disponible'
        
    def devolver_libro(self):
        self.disponible = True
        return 'El libro ha sido devuelto'
    
    # propiedades para acceder a los atributos privados
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor

    

libro1 = Libro('El Principito', 'James Charles')

def imprimir_info(libro):
    print(f'Libro: {libro.titulo}, autor: {libro.autor}')

imprimir_info(libro1)