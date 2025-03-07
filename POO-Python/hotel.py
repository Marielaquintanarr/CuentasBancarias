'''
5. Sistema de Reservas de Hotel 🏨
Objetivo: Administrar habitaciones, clientes y reservas en un hotel.
- Clases:
Habitación (número, tipo, disponibilidad)
Cliente (nombre, identificación)
Reserva (cliente, habitación, fechas, numero)
Desafío: Evita que dos clientes reserven la misma
habitación en la misma fecha.
'''
from datetime import datetime
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.fechas = []

    def asignar_fechas(self, fecha_llegada, fecha_salida):
        self.fechas.append(fecha_llegada)
        self.fechas.append(fecha_salida)

    
    def checar_disponibilidad(self, fecha_llegada, fecha_salida):
        # checar que no se empalme con otra rsv
        # Convertir las fechas a objetos datetime para comparaciones seguras
        fecha_llegada = datetime.strptime(fecha_llegada, "%d/%m/%Y")
        fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y")

        #error
        if self.fechas:
            inicio = self.fechas[0]
            fin = self.fechas[-1]
            if not (fecha_salida <= inicio or fecha_llegada >= fin):
                return False  # Se empalman
            
        # Si no hay empalme, agregar la reserva
        self.fechas.append(fecha_llegada)
        self.fechas.append(fecha_salida)
        return True
        

class Cliente:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre
        self.__identificacion = identificacion

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def identificacion(self):
        return self.__identificacion

# opciones de cuarto 2 -> cuarto sencillo, suite
# habitaciones_sencillas = 501, 502
# habitaciones_sencillas_suite = 503, 504
# opciones de cuarto 3-4 -> cuarto doble, suite
# habitaciones_dobles = 505, 506
# habitaciones_dobles_suite = 507, 508
# opciones de cuarto 3-5 -> cuarto familiar, suite
# habitaciones_sencillas_suite = 509, 510
# habitaciones_sencillas_suite = 511, 512

# Reserva (cliente, habitación, fechas, numero)
habitacion_501 = Habitacion(501, 'Sencilla')
habitacion_502 = Habitacion(502, 'Sencilla Suite')
habitacion_503 = Habitacion(503, 'Doble')
habitacion_504 = Habitacion(504, 'Doble Suite')
habitacion_505 = Habitacion(505, 'Familiar')
habitacion_506 = Habitacion(506, 'Familiar Suite')

habitaciones_sencillas = {habitacion_501, habitacion_502}
habitaciones_dobles = {habitacion_503, habitacion_504}
habitaciones_familiares = {habitacion_505, habitacion_506}

import sys
class Reserva:
    def __init__(self, num_reserva):
        self.num_reserva = num_reserva
        self.datos_de_reserva = dict()
    
    def crear_reserva(self):
        print(f'Porfavor ingrese sus datos: ')
        nombre = input('Nombre: ')
        identificacion = input('Identificacion: ')
        cliente = Cliente(nombre, identificacion)

        numero_de_huespedes = int(input('Ingresa el numero de huespedes: '))
        fecha_llegada = (input('Ingresa la fecha de llegada (dd/mm/aaaa): '))
        fecha_salida = (input('Ingresa la fecha de salida (dd/mm/aaaa): '))
        if numero_de_huespedes <= 2:
            tipo = input('Qué tipo de habitacion desea: a) sencilla b) suite: ')
            if tipo == 'a':
                if habitacion_501.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 501'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()
                    
            else:
                if habitacion_502.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 502'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()

        elif numero_de_huespedes == 3 or numero_de_huespedes == 4:
            tipo = input('Qué tipo de habitacion desea: a) doble b) doble suite: ')
            if tipo == 'a':
                if habitacion_503.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 503'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()

            else:
                if habitacion_504.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 504'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()
        else:
            tipo = input('Qué tipo de habitacion desea: a) familiar b) familiar suite: ')
            if tipo == 'a':
                if habitacion_505.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 505'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()
            else:
                if habitacion_506.checar_disponibilidad(fecha_llegada, fecha_salida):
                    habitacion = 'habitacion 506'
                else:
                    print('Esta habitacion no esta disponible en esas fechas')
                    sys.exit()
        # error
        self.datos_de_reserva[self.num_reserva] = [cliente.nombre, cliente.identificacion, habitacion, numero_de_huespedes, fecha_llegada, fecha_salida]
        print(self.datos_de_reserva)




reserva = Reserva(1233)
reserva.crear_reserva()

reserva = Reserva(1234)
reserva.crear_reserva()

