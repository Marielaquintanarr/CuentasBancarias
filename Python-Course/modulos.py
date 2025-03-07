# todos los archivos que terminan en .py son modulos

# import modulo_saludar

# saludo = modulo_saludar.saludar('Mariela') 
# print(saludo)


# si el modulo estuviera dentro de una carpeta en la misma ruta
#import nombre_carpeta.saludar as m_saludar
#print(m_saludar.saludar('Mariela'))

# si la carpeta esta afuera
import sys
sys.path.append('ruta')