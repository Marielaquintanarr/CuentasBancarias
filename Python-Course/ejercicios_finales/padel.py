'''
Sistema de Reservaciones de Pistas de Pádel 🎾 (aprovechando tus proyectos pasados)

Usar POO para modelar jugadores, partidos y horarios.
Guardar las reservaciones en un archivo TXT o CSV.
Validar horarios disponibles.
'''

# cada reserva es de 1:30
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def convertir_24h(self, hora):
            tiempo = hora.split(':')
            hora = int(tiempo[0])
            minutos = (tiempo[-1][:2])
            AM_PM = (tiempo[-1][-2:])
            if AM_PM.lower() == 'pm' and hora != 12:
                hora += 12
            elif AM_PM.lower() == 'am' and hora == 12:
                hora += 12
            else:
                hora = hora
            
            hora_final = str(hora) + ':' + minutos + AM_PM
            return hora_final
    
    # 1. solicitar rsv
    def hacer_rsv(self, admin, agenda):
        nombre = input('Ingrese el nombre: ')
        num_cancha = int(input('Ingrese el numero de cancha a reservar: '))
        dia = input('Ingrese el dia: ')
        hora = input('Ingrese la hora: ')

        # horario_canchas = ['6:00AM', '11:00PM']
        hora = self.convertir_24h(hora)

        
        if 1==1:

            # 2. autorizar rsv
            if admin.autorizar_rsv(num_cancha, dia, hora, agenda)[0] == False:
                print(admin.autorizar_rsv(num_cancha, dia, hora, agenda)[-1])
            else:
                admin.crear_reserva(nombre, num_cancha, dia, hora, agenda)
        else:
            pass
            #print(f'El horario de nuestras canchas es de {horario_canchas[0]} a {horario_canchas[-1]}')

        
        
# {num_cancha: {dia: hora, hora, hora}, {dia}}

class Admin:
    def autorizar_rsv(self, num_cancha, dia, hora, agenda):

        # que la solicitud 
        # checar si la cancha tiene reservas
        if num_cancha in agenda.reservaciones:
            # checar que este la fecha
            if dia not in agenda.reservaciones[num_cancha]:
                # se puede autorizar crear esa fecha
                return [True, 'Aun no hay una rsv en esa fecha']
            else:
                # checar si en esa fecha ya hay una reserva a esa hora
                if hora not in agenda.reservaciones[num_cancha][dia]:
                    # si no hay se puede crear una
                    return [True, 'Aun no hay una rsv en esa hora']
                else:
                    return [False, 'Ya hay una rsv en esa hora y ese dia']
        else:
            return [False, 'Ese numero de cancha no existe']

    "12/02/2025"
    # 3. ya autorizada se crea la rsv  
    def crear_reserva(self, nombre, num_cancha, dia, hora, agenda):
        if self.autorizar_rsv(num_cancha, dia, hora, agenda)[0]:
            reservacion = Reservacion(nombre, num_cancha, dia, hora)
            
            # si aun no existe fecha
            if self.autorizar_rsv(num_cancha, dia, hora, agenda)[-1] == 'Aun no hay una rsv en esa fecha':
                agenda.reservaciones[reservacion.num_cancha] = {}
                agenda.reservaciones[reservacion.num_cancha][reservacion.dia] = {}
                agenda.reservaciones[reservacion.num_cancha][reservacion.dia][reservacion.hora] = {}
                agenda.reservaciones[reservacion.num_cancha][reservacion.dia][reservacion.hora] = reservacion.nombre
                print('Se ha creado la reserva con exito')
            # si ya existe la fecha
            else:
                agenda.reservaciones[reservacion.num_cancha][reservacion.dia][reservacion.hora] = {}
                agenda.reservaciones[reservacion.num_cancha][reservacion.dia][reservacion.hora] = reservacion.nombre
                print('Se ha creado la reserva con exito')
        else:
            print(self.autorizar_rsv(num_cancha, dia, hora, agenda)[-1])


class Reservacion:
    def __init__(self, nombre, num_cancha, dia, hora):
        self.nombre = nombre
        self.num_cancha = num_cancha 
        self.dia = dia
        self.hora = hora
        
    # despues de crearla
    #reservaciones[num_cancha] = fecha[nombre:]

# horario 6am - 11pm

class Agenda:
    def __init__(self):
        self.reservaciones = {1: {}, 2: {}, 3: {}}



admin = Admin()
agenda = Agenda()
mariela = Jugador('Mariela')
jaime = Jugador('Jaime')

mariela.hacer_rsv(admin, agenda)
jaime.hacer_rsv(admin, agenda)
print(agenda.reservaciones)

'''
(1 y 2 son el num_cancha)
rsvs{
    1 {
        12/02/2025 {
            'Mariela':05:00PM,
            'Jaime':7:00PM,
            'Salomon':9:00PM
        }
        13/02/2025 {
            'Kola':5:00PM,
            'Wesley':7:00PM,
            'Sofia':9:00PM
        }
    },
    2 {
        12/02/2025 {
            'Mariela':05:00PM,
            'Jaime':7:00PM,
            'Salomon':9:00PM
        }
        13/02/2025 {
            'Mariela':05:00PM,
            'Jaime':7:00PM,
            'Salomon':9:00PM
        }
    }
}

'''

