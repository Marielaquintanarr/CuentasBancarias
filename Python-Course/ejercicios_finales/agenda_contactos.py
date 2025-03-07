'''
3. agenda de Contactos (POO + Archivos CSV)
**Descripción:**  
Crea una agenda de contactos donde puedas agregar, buscar y eliminar contactos.

**Requisitos:**  
- Crea una clase `Contacto` con `nombre`, `teléfono` y `correo`.
- Guarda los contactos en un archivo CSV.
- Implementa un menú que permita al usuario administrar los contactos.
'''
import csv
import re

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.agenda = {}
    
    def agregar_contacto(self):
        nombre = input('Ingresa tu nombre: ')
        telefono = input('Ingresa tu telefono: ')
        correo = input('Ingresa tu correo: ')
        contacto = Contacto(nombre, telefono, correo)

        with open('ejercicios_finales//agenda.csv', mode='w', newline='', encoding="utf-8") as archivo:
            escrito = csv.writer(archivo)
            escrito.writerow(f'{contacto.nombre} = telefono: {contacto.telefono}, correo: {contacto.correo}')
    
    def buscar_contanto(self):
        contacto_a_buscar = input('Ingresa el contacto a buscar: ')
        if contacto_a_buscar in self.agenda:
            print(f'{contacto_a_buscar}: {self.agenda[contacto_a_buscar]}')
        else:
            print('no se encontro el contacto')

    def eliminar_contacto(self):
        contacto_a_eliminar = input('Ingresa el contacto a eliminar: ')
        if contacto_a_eliminar in self.agenda:
            del self.agenda[contacto_a_eliminar]
        else:
            print('El contacto no se encontro')





agenda = Agenda()
agenda.agregar_contacto()
agenda.agregar_contacto()

