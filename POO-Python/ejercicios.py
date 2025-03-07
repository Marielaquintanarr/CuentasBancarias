class Estudiante():
    # atributos
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado
    
    def estudiar(self):
        print(f'El estudiante {self.Nombre} está estudiando.')

# crear objeto

nombre = input(str('Ingresa el nombre del alumno: '))
edad = input(str('Ingresa la edad del alumno: '))
grado = input(str('Ingresa el grado del alumno: '))
estado = input(str('El estudiante esta estudianto?: (S/N): '))
estudiante1 = Estudiante(nombre, edad, grado)

if estado == 'S':
    print(f'Nombre del estudiante {estudiante1.Nombre}')
    print(f'Edad del estudiante {estudiante1.Edad}')
    print(f'Grado del estudiante {estudiante1.Grado}')
    estudiante1.estudiar()
else:
    print(f'Nombre del estudiante {estudiante1.Nombre}')
    print(f'Edad del estudiante {estudiante1.Edad}')
    print(f'Grado del estudiante {estudiante1.Grado}')
    estudiante1.estudiar()