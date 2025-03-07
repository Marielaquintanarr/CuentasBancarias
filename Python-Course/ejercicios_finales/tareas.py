'''
### 1. **Sistema de Gestión de Tareas (POO + CSV)**
**Descripción:**  
Crea un programa que administre una lista de tareas. Cada tarea debe tener un `título`, `descripción`, `fecha de vencimiento` y `estado` (pendiente, en progreso, completada).  

**Requisitos:**  
- Usa clases: `Tarea` y `GestorTareas`.
- Permite agregar, eliminar, actualizar y listar tareas.
- Guarda y carga las tareas desde un archivo CSV.
'''

import csv

class Tarea:
    def __init__(self, titulo, descripcion, deadline, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.deadline = deadline
        self.estado = estado

class GestorTareas:
    def __init__(self):
        pass
        
    def crear_tarea(self, titulo, descripcion, deadline, estado):
        tarea = Tarea(titulo, descripcion, deadline, estado)
