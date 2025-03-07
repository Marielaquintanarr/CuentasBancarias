'''
Simulador de Cuenta Bancaria 💰
Clases: CuentaBancaria (titular, saldo, métodos: depositar, retirar, consultar saldo).
'''

class Contacto:
    def __init__(self, nombre, numero_cuenta, banco, dinero):
        self.nombre  = nombre
        self.numero_cuenta = numero_cuenta
        self.banco = banco
        self.dinero = dinero

    def mostrar_persona(self):
        print(f'Nombre: {self.nombre}, Número de cuenta: {self.numero_cuenta}, Banco: {self.banco}, dinero: {self.dinero}')


class CuentaBancaria:
    def __init__(self, nombre, numero_de_cuenta, dinero):
        self.nombre = nombre
        self.numero_de_cuenta = numero_de_cuenta
        self.dinero = dinero
        self.contactos_guardados = {}

    def guardar_contacto(self, nombre, numero_cuenta, banco, dinero):
        contacto = Contacto(nombre, numero_cuenta, banco, dinero)
        self.contactos_guardados[contacto.nombre] = {
            "numero_cuenta": contacto.numero_cuenta,
            "banco": contacto.banco,
            "dinero": contacto.dinero
        } 
    
    def mostrar_contactos_guardados(self):
        for name, data in self.contactos_guardados.items():
            print(f'{name}: {data}')

    def mostrar_contactos(self, nombre_contacto):
        if nombre_contacto in self.contactos_guardados.keys():
            print(f'{nombre_contacto}, datos: {self.contactos_guardados[nombre_contacto]}')

    def depositar(self, nombre_destinatario):
        opcion = input('Selecciona a o b: a) Buscar entre contactos guardados, b) Crear nuevo contacto: ')
        if opcion == 'a':
            if nombre_destinatario in self.contactos_guardados.keys():
                self.mostrar_contactos(nombre_destinatario)
            else:
                'Destinatario no encontrado'
        else:
            nombre_destinatario = input('Ingresa el nombre: ')
            numero_cuenta = input('Ingresa el numero de cuenta: ')
            banco = input('Ingresa el banco: ')
            dinero = 0
            self.guardar_contacto(nombre_destinatario, numero_cuenta, banco, dinero)
        
        # sumar cantidad

        cantidad = int(input('Ingresa la cantidad a transferir: '))
        self.contactos_guardados[nombre_destinatario]["dinero"] += cantidad
        print(f'Se ha depositado ${cantidad} a {nombre_destinatario}')
    
    def consultar_saldo(self):
        print(f'Su saldo es {self.dinero}')

    def retirar(self):
        cantidad = float(input('ingresa la cantidad a retirar: '))
        self.dinero -= cantidad
        print(f'Se han retirado ${cantidad}')
        self.consultar_saldo()

anapau = Contacto('Ana Pau', 28288292, 'BBVA', 10000)           

cuenta_mariela = CuentaBancaria('Mariela', 29928383929, 100000)
# cuenta_mariela.guardar_contacto('Ana Pau', 2998282, 'BBVA', 1000)
# cuenta_mariela.mostrar_contactos_guardados()
# cuenta_mariela.depositar('Ana Pau')
# cuenta_mariela.mostrar_contactos_guardados()
cuenta_mariela.retirar()
