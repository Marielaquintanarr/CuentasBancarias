from abc import ABC

class Usuario(ABC):
    def __init__(self, id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol

class Medico(Usuario):
    def __init__(self, id, nombre, rol, horario):
        super().__init__(id, nombre, rol)
        self.horario = horario  
        self.directorio_citas = {}
    
    def revisarCitas(self):
        print('Citas agendadas:')
        for fecha, citas in self.directorio_citas.items():
            print(f'Fecha: {fecha}')
            for cita in citas:
                print(f'  - {cita[0]} a las {cita[1]}: {cita[2]}. Estatus: {cita[-1]}')

    def aceptarCitas(self, fecha, hora):
        AM_PM = hora[-2:]  #
        hora_sin_ampm = hora[:-2]  # "06:00"
        
        # solo agarrar el int
        hora_int = int(hora_sin_ampm.split(":")[0])

        # de 12h a 24h
        if AM_PM == "PM" and hora_int != 12:
            hora_int += 12
        elif AM_PM == "AM" and hora_int == 12:
            hora_int = 0  

        # esta dentro del horario del doctor
        if self.horario[0] <= hora_int < self.horario[1]:  
            # si ya hay cita a esa hora y en esa fecha
            if fecha in self.directorio_citas:
                for cita in self.directorio_citas[fecha]:
                    if cita[1] == hora: 
                        return False  
            return True  
        return False  
    
    # buscar por fecha y nombre al paciente
    def actualizarEstadoConsulta(self):
        paciente = input('Ingrese el nombre del paciente: ')
        fecha = input('Ingrese la fecha de consulta: ')

        if fecha not in self.directorio_citas:
            print('No hay citas registradas en esa fecha.')
            return
        
        for cita in self.directorio_citas[fecha]:
            if cita[0] == paciente:
                status = input('Ingrese el nuevo status de la consulta: ')
                cita[-1] = status  
                print('Estado actualizado con éxito.')
                return

        print('No se encontró una cita para el paciente: {paciente} en la fecha: {fecha}.')


class Enfermera(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)
        self.registro_signos_vitales = {}
        # Mariela : [fecha, signos], [fecha, signos], [fecha, signos]

    def actualizarEstadoConsulta(self):
        paciente = input('Ingrese el nombre del paciente: ')
        fecha = input('Ingrese la fecha de consulta: ')

        if fecha not in self.directorio_citas:
            print('No hay citas registradas en esa fecha.')
            return
        
        for cita in self.directorio_citas[fecha]:
            if cita[0] == paciente:
                status = input('Ingrese el nuevo status de la consulta: ')
                cita[-1] = status  
                print('Estado actualizado con éxito.')
                return

        print(f'No se encontró una cita para el paciente: {paciente} en la fecha: {fecha}.')

    
    def registrarSignosVitales(self):
        nombre = input('Ingresa el nombre del paciente: ')
        fecha = input('Ingresa la fecha: ')
        signos_vitales = input('Ingresa los signos vitales: ')

        if nombre not in self.registro_signos_vitales:
            self.registro_signos_vitales[nombre] = []
        self.registro_signos_vitales[nombre].append([fecha, signos_vitales])

    def asistirMedico(self):
        pass



class Paciente(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)
        self.historial_citas = {}

    def agendarCita(self, medico):
        nombre = input('Ingrese su nombre: ')
        fecha = input('Ingrese la fecha (DD/MM/AAAA): ')
        hora = input('Ingrese la hora (ej. 06:00PM): ')
        motivo_de_consulta = input('Ingrese su motivo de consulta: ')

        if medico.aceptarCitas(fecha, hora):
            cita = Cita(nombre, fecha, hora, motivo_de_consulta)
            if fecha not in medico.directorio_citas:
                medico.directorio_citas[cita.fecha] = []
            medico.directorio_citas[cita.fecha].append([cita.nombre, cita.hora, cita.motivo_de_consulta, cita.estado])
            print('Su cita ha sido agendada.')
        else:
            print(f'Su cita NO se pudo agendar. El horario del doctor {medico.nombre} es de {medico.horario[0]}:00 - {medico.horario[1]}:00')

    
    def verEstadoCitas(self, medico):
        fecha = input('Ingrese la fecha de la cita que desea consultar: ')
        if fecha in medico.directorio_citas:
            print(medico.directorio_citas[fecha])
        else:
            print('No hay ninguna cita agendada en esa fecha')


class Cita:
    def __init__(self, nombre, fecha, hora, motivo_de_consulta):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.motivo_de_consulta = motivo_de_consulta
        self.estado = ''


class Administrador(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)

    def gestionarHorarios(self):
        pass

    def gestionarCitas(self):
        pass

def main():
    medico = Medico(1, 'Mariela', 'Medico', [8, 18])  
    paciente = Paciente(2, 'Pablo', 'Paciente')
    paciente.agendarCita(medico)
    print('')
    medico.revisarCitas()

main()