class Reporte:
    def __init__(self, __titulo, __autor, __contenido):
        self.__titulo = __titulo
        self.__autor = __autor
        self.__contenido = __contenido

    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, value):
        self.__titulo = value
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, value):
        self.__autor = value

    def get_contenido(self):
        return self.__contenido
    
    def set_contenido(self, value):
        self.__contenido = value

    def generarContenido(self):
        return f'Titulo:{self.get_titulo()}\n Autor: {self.get_autor()}\n Contenido:\n {self.get_contenido()}'

class ReporteArchivo:
    def guardar(self, reporte, nombreArchivo):
        with open(f'practicas_output/{nombreArchivo}.txt', 'w') as archivo:
            archivo.writelines(reporte.generarContenido())

class Main:
    def crear_reporte(self):
        titulo = input('ingresa el titulo: ')
        autor = input('ingresa el titulo: ')
        contenido = input('ingresa el titulo: ')
        reporte = Reporte(titulo, autor, contenido)
        print('El reporte se a creado')
    
    def acceder_contenido_reporte(self):
        reporte = input('Ingresa el reporte: ')
        print(reporte.generarContenido())
    
    def guardar_reporte(self):
        reporte = ReporteArchivo()
        r = input('Ingrese el reporte a guardar: ')
        t = input('Ingrese el titulo: ')
        reporte.guardar(r, t)
        print('El reporte ha sido guardado')



main = Main()