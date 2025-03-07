'''
Simulador de Cajero Automático
Crea una clase CuentaBancaria con saldo, nombre y número de cuenta.
Métodos para depositar, retirar y consultar saldo.
Guarda los movimientos en un archivo txt.
'''
import os
from datetime import datetime
from abc import ABC, abstractmethod
import random as rnd
class Admin:
    def generar_cvv(self):
        cvv = rnd.randint(100, 999)
        return cvv
    
    def generar_numero_cuenta(self):
        numero_cuenta = rnd.randint(10**11, (10**12)-1)
        return numero_cuenta

    def generar_numero(self):
        numero = rnd.randint(10**11, (10**12)-1)
        return numero


class CuentaBancaria:
    def __init__(self, admin, nombre):
        self.nombre = nombre
        self.saldo = 0
        self.numero_cuenta = admin.generar_numero_cuenta()
        # {numero_cuenta_obj : nombre}
        self.contactos = {}
        self.tarjetas = []

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Saldo: {self.saldo}, Numero de cuenta: {self.numero_cuenta}')

    def crearTarjetaDebito(self, admin):
        cvv = admin.generar_cvv()
        numero = admin.generar_numero()
        tarjeta_debito = TarjetaDebito(numero, cvv, self.nombre)
        print('Se ha creado tu tarjeta con exito')
        tarjeta_debito.mostrar_datos()
        self.tarjetas.append(tarjeta_debito)

    def mostrar_contactos(self):
        for num, nombre in self.contactos:
            print(f'Numero de cuenta: {num} Nombre: {nombre}' + '\n')

    def crearTarjetaCredito(self, admin):
        cvv = admin.generar_cvv()
        numero = admin.generar_numero()
        fecha_de_pago = input('¿Cuando desea que sea su fecha de pago? a) Los primeros de cada mes b) Las quincenas de cada mes: ')
    
        if fecha_de_pago == 'a':
            fecha_de_corte = 'a'
            print('Su fecha de corte sera los 22 de cada mes')
        else:
            fecha_de_corte = 'b'
            print('Su fecha de corte sera el último dia de cada mes')
        tarjeta_credito = TarjetaCredito(numero, cvv, self.nombre, fecha_de_corte, fecha_de_pago)
        print('Se ha creado tu terjeta con éxito')
        tarjeta_credito.mostrar_datos()
        self.tarjetas.append(tarjeta_credito)

    def depositar(self, cuenta, monto):
        path = '/Users/marielaquintanar/Desktop/cursos/Python-Course/ejercicios_finales'
        archive = 'Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt'
        fecha = datetime.now()
        fecha = fecha.strftime("%d/%m/%Y")

        self.saldo += monto
        tarjeta_debito = self.tarjetas[0]
        tarjeta_debito.saldo += monto

        print(f'Su saldo ahora es de ${tarjeta_debito.saldo}')
        if archive not in os.listdir(path):
            # crearlo
            with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'w') as archivo:
                archivo.writelines(f'fecha: {fecha}' + '\n' + 'Deposito'+ '\n'+ f'+ {monto}' + '\n' + '\n')
        else:
            # escribir en el que ya esta
            with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'a') as archivo:
                archivo.writelines(f'fecha: {fecha}' + '\n' + 'Deposito' + '\n' + f'+ {monto}' + '\n' + '\n')
       
    def retirar(self, cuenta, monto):
        path = '/Users/marielaquintanar/Desktop/cursos/Python-Course/ejercicios_finales'
        fecha = datetime.now()
        fecha = fecha.strftime("%d/%m/%Y")

        self.saldo -= monto
        tarjeta_debito = self.tarjetas[0]
        archive = 'Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt'

        if monto > self.saldo:
            print(f'El monto excede su saldo. Su saldo actual es de ${cuenta.numero_cuenta}')
        else:
            self.saldo -= monto
            tarjeta_debito.saldo -= monto
            print(f'Se han retirado ${monto} de su cuenta')
            if archive not in os.listdir(path):
                # no existe
                with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'w') as archivo:
                    archivo.writelines(f'Fecha: {fecha}' + '\n' +  'Retiro' + '\n' + f'- {monto}' + '\n' + '\n')
            else:
                with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'a') as archivo:
                    archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Retiro' + '\n' +  f'- {monto}' + '\n' + '\n')

    def transferir(self, cuenta, cuentas_creadas):
        fecha = datetime.now()
        fecha = fecha.strftime("%d/%m/%Y")
        path = '/Users/marielaquintanar/Desktop/cursos/Python-Course/ejercicios_finales'
        # contactos

        monto = int(input('Ingresa el monto: '))
        concepto = input('Concepto: ')
        
        # no se puede hacer la transeferencia
        if monto > cuenta.saldo or not cuentas_creadas:
            print(f'El monto excede el saldo actual es de: {cuenta.saldo}')
        else:
            # numero de cuenta del destinatario
            opcion = input('Desea a) transferir a un contacto guardado b) crear contacto y transferir: ')
            if opcion == 'a' and self.contactos:
                self.mostrar_contactos()
                nombre_destinatario = input('Ingrese el nombre del destinatario: ')
                # se hace la transeferencia
                cuenta.saldo -= monto
                cuenta_destinatario.saldo += monto
                # hacer los archivos
                archive = 'Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt'
                archive2 = 'Movimientos_de_cuenta' + f'{cuenta_destinatario.numero_cuenta}.txt'

                if archive not in os.listdir(path) and archive2 not in os.listdir(path):
                    with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'w') as archivo:
                        archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta.nombre} '+ '\n' + f'{cuenta.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'- {monto}' + '\n' + '\n')

                    with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta_destinatario.numero_cuenta}.txt', 'w') as archivo:
                        archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta_destinatario.nombre}' + '\n' + f'{cuenta_destinatario.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'+ {monto}' + '\n' + '\n')
                    print(f'Se han tranferido con éxito ${monto} a {cuenta_destinatario.nombre}')
                else:
                    with open(f'{path}/Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt', 'a') as archivo:
                        archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta.nombre}' + '\n' + f'{cuenta.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'- {monto}' + '\n' + '\n')

                    with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta_destinatario.numero_cuenta}.txt', 'a') as archivo:
                        archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta_destinatario.nombre}' + '\n' + f'{cuenta_destinatario.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'+ {monto}' + '\n' + '\n')
                    print(f'Se han tranferido con éxito ${monto} a {cuenta_destinatario.nombre}')
            elif opcion == 'b':
                nombre_destinatario = input('Ingrese el nombre del destinatario: ')
                if nombre_destinatario in cuentas_creadas.values():
                    for cuenta, nombre in cuentas_creadas.items():
                        if nombre == nombre_destinatario:
                            cuenta_destinatario = cuenta

                            cuenta.saldo -= monto
                            cuenta_destinatario.saldo += monto
                            # hacer los archivos
                            archive = 'Movimientos_de_cuenta' + f'{cuenta.numero_cuenta}.txt'
                            archive2 = 'Movimientos_de_cuenta' + f'{cuenta_destinatario.numero_cuenta}.txt'

                            if archive not in os.listdir(path) and archive2 not in os.listdir(path):
                                with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta.numero_cuenta}.txt', 'w') as archivo:
                                    archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta.nombre}'+ '\n' + f'{cuenta.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'- {monto}' + '\n' + '\n')

                                with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta_destinatario.numero_cuenta}.txt', 'w') as archivo:
                                    archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta_destinatario.nombre}' + '\n' + f'{cuenta_destinatario.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'+ {monto}' + '\n' + '\n')
                                print(f'Se han tranferido con éxito ${monto} a {cuenta_destinatario.nombre}')
                            else:
                                with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta.numero_cuenta}.txt', 'a') as archivo:
                                    archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta.nombre}' + '\n' + f'{cuenta.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'- {monto}' + '\n' + '\n')

                                with open(f'{path}/Movimientos_de_cuenta: ' + f'{cuenta_destinatario.numero_cuenta}.txt', 'a') as archivo:
                                    archivo.writelines(f'Fecha: {fecha}' + '\n' + 'Transferencia' + '\n' + f'{cuenta_destinatario.nombre}' + '\n' + f'{cuenta_destinatario.numero_cuenta}' + '\n' + f'Concepto: {concepto}' + '\n' + f'+ {monto}' + '\n' + '\n')
                                print(f'Se han tranferido con éxito ${monto} a {cuenta_destinatario.nombre}')
                        else:
                            continue
                else:
                    print('No se encontro el destinatario')
            else:
                print('Solo hay opcion a y b')


    def consultar_saldo(self, tarjeta):
        print(f'Su saldo es de: {tarjeta.saldo}')

    def consultar_movimientos(self, tarjeta):
        archivo = f'Movimientos_de_cuenta' + f'{tarjeta.numero}.txt'
        path = '/Users/marielaquintanar/Desktop/cursos/Python-Course/ejercicios_finales'
        if archivo in os.listdir(path):
            with open(f'{path}/Movimientos_de_cuenta' + f'{tarjeta.numero}.txt', 'w') as archivo:
                print(archivo.read())
        else:
            print('Aun no se hacen movimientos')

class Tarjeta(ABC):
    def __init__(self):
        self.numero = 0
        self.cvv = 0
        self.saldo = 0
        self.propietario = ''
    
    @abstractmethod
    def mostrar_datos(self, numero, fecha, cvv, saldo):
        print(f'Numero de tarjeta: {self.numero}')
        print(f'cvv: {self.cvv}')
        print(f'Saldo: {self.saldo}')

class TarjetaDebito(Tarjeta):
    def __init__(self,  numero, cvv, propietario):
        super().__init__()
        self.numero = numero
        self.cvv = cvv
        self.saldo = 0
        self.propietario = propietario

    def mostrar_datos(self):
        print(f'Numero de tarjeta: {self.numero}')
        print(f'cvv: {self.cvv}')
        print(f'Saldo: {self.saldo}')

class TarjetaCredito(Tarjeta):
    def __init__(self, numero, cvv, propietario, fecha_corte, fecha_pago):
        super().__init__()
        self.numero = numero
        self.cvv = cvv
        self.saldo = 0
        self.propietario = propietario
        self.puntos = 0
        self.linea_de_credito = 0
        self.linea_de_credito_usada = 0
        self.fecha_corte = fecha_corte
        self.fecha_pago = fecha_pago

    def mostrar_datos(self):
        print(f'Numero de tarjeta: {self.numero}')
        print(f'cvv: {self.cvv}')
        print(f'Saldo: {self.saldo}')
        print(f'Numero de tarjeta: {self.numero}')
        print(f'Fecha: {self.fecha}')
        print(f'cvv: {self.cvv}')
        print(f'Puntos: {self.puntos}')
        print(f'Linea de credito: {self.linea_de_credito}')
        print(f'Fecha corte: {self.fecha_corte}')
        print(f'Fecha de pago: {self.fecha_pago}')
    
    
    def pagar_con_tarjeta(self, monto):
        if monto <= (self.linea_de_credito - self.linea_de_credito_usada):
            self.linea_de_credito_usada += monto
        else:
            print('Se excedio la linea de credito')

    def pagar_tarjeta(self, monto):
        if monto <= self.linea_de_credito_usada:
            self.linea_de_credito_usada = self.linea_de_credito_usada - monto
        else:
            print('El monto ingresado excede la linea de credito utilizada')

cuentas_creadas = {}
admin = Admin()

cuenta1 = CuentaBancaria(admin, 'Mariela')
cuentas_creadas[cuenta1] = cuenta1.nombre
cuenta2 = CuentaBancaria(admin, 'Jaime')
cuentas_creadas[cuenta2] = cuenta2.nombre

cuenta1.mostrar_info()
cuenta2.mostrar_info()

debito1 = cuenta1.crearTarjetaDebito(admin)
# #debito2 = cuenta2.crearTarjetaDebito(admin)

cuenta1.depositar(cuenta1, 500)
cuenta1.mostrar_info()
cuenta1.transferir(cuenta1, cuentas_creadas)

