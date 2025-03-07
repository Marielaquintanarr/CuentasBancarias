'''
📂 1. Gestor de Notas
Descripción: Un programa que permite crear, leer, actualizar y 
eliminar notas almacenadas en archivos de texto.
Conceptos clave:
✔ Clases (Nota, GestorNotas)
✔ CRUD (Create, Read, Update, Delete) con archivos .txt

Extras: Agregar etiquetas a las notas y permitir búsqueda por 
palabras clave.
'''

'''
crear nota


'''
import os
import sys

class Nota:
    def __init__(self, titulo, fecha, contenido):
        self.titulo = titulo
        self.fecha = fecha
        self.contenido =  contenido
    
    def crear(self):
        with open(f'ejercicio//{self.titulo}.txt', 'w') as archivo:
            archivo.writelines([f'{self.titulo}\n', f'{self.fecha}\n', f'{self.contenido}\n'])
    
    def update(self):
        with open('ejercicio//nota.txt', 'w') as archivo:
            #archivo.write('')
            pass
    
    def leer(self):
        with open('ejercicio//nota.txt') as archivo:
            print(archivo.read())


class GestorNotas:
    def __init__(self):
        self.notas = set()
    
    def gestionar(self):
        while True:
            opcion = input('a) desea crear una nota, b) desea borrar una nota, c) desdea modificar una nota, d) desea leer una nota e) exit: ')
            if opcion == 'a':
                titulo = input('Ingrese el titulo de la nota: ')
                fecha = input('ingrese la fecha en formato dd/mm/aaa: ')
                contenido = input('Ingresa el contenido: ')

                nota = Nota(titulo, fecha, contenido)
                nota.crear()
                self.notas.add(nota)

            elif opcion == 'b':
                titulo = input('Ingrese el titulo de la nota: ')
                ruta = f"ejercicio//{titulo}.txt"
                if os.path.exists(ruta):
                    os.remove(ruta)
                    print("Archivo eliminado correctamente.")
                else:
                    print("El archivo no existe.")

            elif opcion == 'c':
                titulo = input('Ingrese el titulo de la nota: ')
                nuevo_contenido = input('Ingresa el contenido nuevo: ')
                if os.path.exists(f'ejercicio//{titulo}.txt'):
                    with open(f'ejercicio//{titulo}.txt', 'w') as archivo:
                        archivo.writelines(nuevo_contenido)
                else:
                    print("El archivo no existe.")

            elif opcion == 'd':
                titulo = input('Ingrese el titulo de la nota: ')
                if os.path.exists(f'ejercicio//{titulo}.txt'):
                    with open(f'ejercicio//{titulo}.txt', 'r') as archivo:
                        print(archivo.read())
                else:
                    print("El archivo no existe.")

            else:
                break

gestor = GestorNotas()
gestor.gestionar()         


    




            
