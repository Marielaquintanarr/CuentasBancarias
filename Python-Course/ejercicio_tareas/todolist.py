'''
📜 2. Registro de Tareas Pendientes (To-Do List)
Descripción: Una aplicación que permite añadir tareas, marcarlas como completadas y guardarlas en un archivo.
Conceptos clave:
✔ Manejo de listas de tareas con archivos
✔ Uso de fechas y formateo de salida (datetime)

Extras: Implementar una opción para ordenar tareas por prioridad o fecha.
'''

class Tareas:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.status = False
    
    def crear_tarea(self):
        pass

