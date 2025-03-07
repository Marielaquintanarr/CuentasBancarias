'''
9. Administrador de Archivos
Objetivo: Practicar abstracción y polimorfismo.
Descripción:
Diseña una clase base Archivo con métodos como abrir, leer, y cerrar.
Implementa clases derivadas como ArchivoTexto y ArchivoImagen.
Simula operaciones como leer un archivo de texto y visualizar una imagen.
'''
from abc import ABC, abstractmethod

class Archivo(ABC):
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio
    
    def abrir(self):
        pass

    def leer(self):
        pass

    def cerrar(self):
        pass


class ArchivoTexto(Archivo):
    def __init__(self, nombre, espacio, mime, contenido):
        super().__init__(nombre, espacio)
        self.mime = mime
        self.contenido = contenido
    
    def abrir(self):
        print(f'Se ha abierto el archivo: {self.nombre}.{self.mime}, {self.espacio} MB')

    def leer(self):
        print(f'{self.contenido}')
    
    def cerrar(self):
        print(f'Se esta cerrando el archivo {self.nombre}...')

class ArchivoImagen(Archivo):
    def __init__(self, nombre, espacio, mime, tamaño):
        super().__init__(nombre, espacio)
        self.tamaño = tamaño
        self.mime = mime
    
    def abrir(self):
        print(f'Se ha abierto el archivo: {self.nombre}.{self.mime}, {self.espacio} MB, tamaño: {self.tamaño}')

    def leer(self):
        print('Se abrio la imagen')
    
    def cerrar(self):
        print(f'Se esta cerrando el archivo {self.nombre}...')

archivo1 = ArchivoTexto('Resumen', '30', 'pdf', 'Diseña una clase base Archivo con métodos como abrir, leer, y cerrar. Implementa clases derivadas como ArchivoTexto y ArchivoImagen. Simula operaciones como leer un archivo de texto y visualizar una imagen.')
archivo2 = ArchivoImagen('Logo', '35', 'png', 'mediana')

archivo1.abrir()
archivo2.abrir()

        