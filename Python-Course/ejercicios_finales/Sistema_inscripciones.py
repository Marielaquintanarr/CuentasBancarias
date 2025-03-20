# hacer un sistema como iris
# primero hacer diagrama de clases
# Colas (Queue) → Lista de espera para cupos limitados.
# Pilas (Stack) → Historial de cambios en inscripciones.

from abc import ABC, abstractmethod

import random as rd
class Usuario(ABC):
    def generar_id(self):
            id = rd.randint(10000, 999999)
            return f'A0{id}'
    
    def __init__(self, nombre):
        self.matricula = self.generar_id()
        self.nombre = nombre

class Estudiante(Usuario):
    def generar_id(self):
         return super().generar_id()
    
    def __init__(self, nombre, semestre):
        super().__init__(nombre)
        self.semestre = semestre
        # materias {nombre: nivel}
        self.materias = {}
        # [{'Miercoles', 'Viernes'}, [[materia, maestro], ['12:00PM', '18:00PM']]]}
        # {lunes : [[materia, maestro], ['12:00PM', '18:00PM']], miercoles: [[materia, maestro], ['12:00PM', '18:00PM']]}
        self.horario_alumno = {}
        self.matricula = self.generar_id()

    def mostrar_datos(self):
        print(f'Matricula: {self.matricula}')
        print(f'Nombre: {self.nombre}')
        print(f'{self.horario_alumno}')

class Profesor(Usuario):
    def generar_id(self):
         return super().generar_id()
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.matricula = self.generar_id()

class Materia:
    def generar_id(self):
        id = rd.randint(1000, 10000)
        return id
    
    def __init__(self, nombre, nivel, semestre):
        self.id = self.generar_id()
        self.nombre = nombre
        self.nivel = nivel
        self.semestre = semestre
    def mostrar_materias(self):
        print(f'Id: {self.id}')
        print(f'Materia: {self.nombre}{self.nivel}')
        print(f'Semestre: {self.semestre}')

class Horario:
    def generar_id(self):
        id = rd.randint(1000, 10000)
        return id
    
    def __init__(self):
        self.id = self.generar_id()
        self.horario = {}
    

class Sistema:
    def __init__(self):
        self.horarios_disponibles = []
    
    def crear_horario(self, sistema):
        dias = []
        dia1 = input('Ingrese dia 1: ')
        dia2 = input('Ingrese dia 2: ')
        dias.append(dia1)
        dias.append(dia2)

        hora_inicio =input('Ingrese la hora de inicio: ')
        hora_fin =input('Ingrese la hora de fin: ')

        horario = Horario()
        id = horario.generar_id()
        horario.horario[id] = [dias, [hora_inicio, hora_fin]]
        sistema.horarios_disponibles.append(horario.horario)
        return horario

    def mostrar_horarios(self):
        print(self.horarios_disponibles)
    
    def autorizar_estudiante(self, grupo, estudiante):
        if grupo.materia.nivel == 1 or grupo.materia.nivel == 0:
            return [True, 'Se inscribio con éxito']
        else:
            max_nivel = 0
            for materia, nivel in estudiante.materias.items():
                if grupo.materia.nombre == materia:
                    max_nivel = max(max_nivel, nivel)
                
            if max_nivel + 1 == grupo.materia.nivel:
                res = [True, 'Se inscribio con éxito']
                return res
            elif max_nivel + 1 > grupo.materia.nivel:
                res = [False, 'ya se curso la materia']
                return res
            else:
                res = [False, 'Error: Aún no se puede cursar la materia']
                return res
            
    def checar_que_no_se_empalme(self, grupo, estudiante):
        autorizar_horario = [True, 'Se ha inscrito con éxito']
        data = list(grupo.horario.horario.values())[-1]
        dias_salon = data[0]
        horas = data[-1]
        hora_inicio_o = horas[0]
        hora_fin_o = horas[-1]
        hora_inicio = hora_inicio_o.split(':')
        hora_inicio = int(hora_inicio[0])
        hora_fin = hora_fin_o.split(':')
        hora_fin = int(hora_fin[0])

        # si esta vacio el horario del alumno se puede inscribir
        if len(estudiante.horario_alumno) == 0:
            autorizar_horario = [True, 'Se ha inscrito con éxito']
        else:
            for dia_salon in dias_salon:
                # si el dia del grupo ya esta en el horario del alumno
                if dia_salon in estudiante.horario_alumno.keys():
                    # info = [['Cálculo I', 'Gerardo Salinas'], ['7:00AM', '11:00AM']]
                    info = estudiante.horario_alumno[dia_salon][0]
                    materia = info[0][0]
                    hora_inicio_alumno = info[-1][0]
                    hora_fin_alumno = info[-1][-1]
                    hora_inicio_alumno = hora_inicio_alumno.split(':')
                    hora_inicio_alumno = int(hora_inicio_alumno[0])
                    hora_fin_alumno = hora_fin_alumno.split(':')
                    hora_fin_alumno = int(hora_fin_alumno[0])

                    # checar si es a la misma hora
                    if not (hora_fin_alumno <= hora_inicio or hora_inicio_alumno >= hora_fin):
                        # se empalman
                        autorizar_horario = [False, f'Se empalma la materia {grupo.materia.nombre} el dia {dia_salon}, hora: {hora_inicio}:00 - {hora_fin}:00 con la materia: {materia} hora: {hora_inicio_alumno}:00 - {hora_fin_alumno}:00']
                        return autorizar_horario
                    else:
                        # NO se empalman
                        autorizar_horario = [True, 'Se ha inscrito con éxito']
                        return autorizar_horario
                else:
                    autorizar_horario = [True, 'Se ha inscrito con éxito']
                    return autorizar_horario
        return autorizar_horario

    def inscribir_a_grupo(self, grupo, estudiante):
        if self.autorizar_estudiante(grupo, estudiante)[0] == True:
            if self.checar_que_no_se_empalme(grupo, estudiante)[0] == True:
                data = list(grupo.horario.horario.values())[-1]
                dias_salon = data[0]
                horas = data[-1]
                hora_inicio_o = horas[0]
                hora_fin_o = horas[-1]
                hora_inicio = hora_inicio_o.split(':')
                hora_inicio = int(hora_inicio[0])
                hora_fin = hora_fin_o.split(':')
                hora_fin = int(hora_fin[0])

                for dia_salon in dias_salon:
                    # si ya existe el dia
                    if dia_salon in estudiante.horario_alumno.keys():
                        grupo.estudiantes_inscritos.add(estudiante)
                        estudiante.horario_alumno[dia_salon].append([[grupo.materia.nombre, grupo.maestro.nombre], [hora_inicio_o, hora_fin_o]])
                        print(self.checar_que_no_se_empalme(grupo, estudiante)[-1])
                    else:
                        grupo.estudiantes_inscritos.add(estudiante)
                        estudiante.horario_alumno[dia_salon] = []
                        estudiante.horario_alumno[dia_salon].append([[grupo.materia.nombre, grupo.maestro.nombre], [hora_inicio_o, hora_fin_o]])
                        print(self.checar_que_no_se_empalme(grupo, estudiante)[-1])
            else:
                print(self.checar_que_no_se_empalme(grupo, estudiante)[-1])
        else:
            print(f'{self.autorizar_estudiante(grupo, estudiante)[-1]}')
 
class Grupo:
    def generar_id(self):
        id = rd.randint(1000, 10000)
        return id
     
    def __init__(self, maestro, materia, capacidad, horario):
        self.id = self.generar_id()
        self.maestro = maestro
        self.materia = materia
        self.capacidad = capacidad
        self.estudiantes_inscritos = set()
        self.horario = horario
    
    def mostrar_datos(self):
        print(f'Id: {self.id}')
        print(f'Maestro: {self.maestro.nombre}')
        print(f'Materia: {self.materia.nombre}')
        print(f'Capacidad: {self.capacidad}')
        print(f'Horario del salon: {self.horario.horario}')
        print(f'Estudiantes inscritos: ')
        for estudiante in self.estudiantes_inscritos:
            print(f'{estudiante.nombre}')


# horario = {dia : [hora inicio, hora fin]}
sistema = Sistema()
materia1 = Materia('Cálculo I', 1, 'Sexto')
materia2 = Materia('Física I', 1, 'Sexto')
materia3 = Materia('Física II', 2, 'Sexto')

horario1 = sistema.crear_horario(sistema)
horario2 = sistema.crear_horario(sistema)

maestro1 = Profesor('Gerardo Salinas')
maestro2 = Profesor('Luisa Portillo')

grupo104 = Grupo(maestro1, materia1, 25, horario1)
grupo105 = Grupo(maestro2, materia3, 25, horario2)


estudiante1 = Estudiante('Mariela', 'Sexto')


sistema.inscribir_a_grupo(grupo104, estudiante1)
estudiante1.mostrar_datos()
print('')

sistema.inscribir_a_grupo(grupo105, estudiante1)
estudiante1.mostrar_datos()




    