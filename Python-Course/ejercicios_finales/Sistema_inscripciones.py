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
        self.matricula = self.generar_id()

    def mostrar_datos(self):
        print(f'Matricula: {self.matricula}')
        print(f'Nombre: {self.nombre}')

class Profesor(Usuario):
    def generar_id(self):
         return super().generar_id()
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.matricula = self.generar_id()

class Materia:
    def __init__(self, id, nombre, nivel, semestre):
        self.id = id
        self.nombre = nombre
        self.nivel = nivel
        self.semestre = semestre
    def mostrar_materias(self):
        print(f'Nombre: {self.id}')
        print(f'Nombre: {self.nombre}{self.nivel}')
        print(f'Nombre: {self.semestre}')

class Grupo:
    def generar_id(self):
        id = rd.randint(1000, 10000)
        return id
     
    def __init__(self, maestro, materia, capacidad):
        self.id = self.generar_id()
        self.maestro = maestro
        self.materia = materia
        self.capacidad = capacidad
        self.estudiante = {}

class Sistema:
    def __init__(self):
        pass

    def inscribir_a_grupo(self, grupo, estudiante):
        def autorizar_estudiante(self):
            if grupo.materia.nivel == 1 or grupo.material.nivel == 0:
                return True
            else:
                max_nivel = 0
                for materia, nivel in estudiante.materias.items():
                    if grupo.materia.nombre == materia:
                        max_nivel = max(max_nivel, nivel)
                
                if max_nivel + 1 == grupo.materia.nivel:
                    return [True, 'Si se puede insrcibir']
                elif max_nivel + 1 > grupo.materia.nivel:
                    return [False, 'Ya se curso la materia']
                else:
                    return [False, 'Aun no se puede cursar la materia']
        
        
    






