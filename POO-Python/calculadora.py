'''
Gestor de Contactos 📞
Clases: Contacto (nombre, teléfono, email), Agenda (lista de contactos, agregar, eliminar, buscar).
'''

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        # diccionario
        # nombre : [telefono, email]
        self.lista_de_contactos = {}

    def agregar_contactos(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.lista_de_contactos[contacto.nombre] = [contacto.telefono, contacto.email]

    def eliminar_contactos(self):
        contacto_a_eliminar = input('Ingresa el contacto a eliminar: ')
        if contacto_a_eliminar in self.lista_de_contactos:
            del self.lista_de_contactos[contacto_a_eliminar]
        else:
            print('No existe el contacto')


    def buscar_contacto(self):
        nombre_contacto = input('Ingresa el contacto a buscar: ')
        for nombre, datos in self.lista_de_contactos.items():
            if nombre ==  nombre_contacto:
                print(f'{nombre}: {datos}')
            else:
                print('Contacto no encontrado')
    
    def mostrar_contactos(self):
        if not self.lista_de_contactos:
            print('La agenda esta vacía')
        for items, values in self.lista_de_contactos.items():
            print(f'{items} : {values}')
 


agenda = Agenda()
agenda.agregar_contactos('Mariela Quintanar', 3334510073, 'marielaqntrr@gmail.com')
agenda.mostrar_contactos()
agenda.eliminar_contactos()
agenda.mostrar_contactos()


        