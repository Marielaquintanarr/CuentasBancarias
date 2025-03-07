'''
Descripción:
Define una clase base Empleado con atributos como nombre, edad, y métodos como calcular_sueldo.
Crea clases derivadas como EmpleadoPorHoras y EmpleadoAsalariado, que calculen el sueldo de manera diferente.
Implementa un método para imprimir un informe con todos los empleados, sus roles, y su sueldo.
'''

class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, rol, dias_trabajados, pago_por_hora):
        super().__init__(nombre, edad)
        self.rol = rol
        self.dias_trabajados = dias_trabajados
        self.pago_por_hora = pago_por_hora
    
    def calcular_sueldo(self):
        salario = self.dias_trabajados*self.pago_por_hora*8
        return salario

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, edad, rol):
        super().__init__(nombre, edad)
        self.rol = rol 
    
    def calcular_sueldo(self):
        print(13,456.00)


empleado1 = EmpleadoPorHoras('Mariela', 20, 'DB Support Engineer', 30, 70)
empleado2 = EmpleadoAsalariado('Jaime', 20, 'UX Designer')

def imprimir_info(empleado):
    salario = (empleado.calcular_sueldo())
    print(f'Nombre empleado: {empleado.nombre}, edad: {empleado.edad}, rol: {empleado.rol}, salario: {salario}')


imprimir_info(empleado1)





        