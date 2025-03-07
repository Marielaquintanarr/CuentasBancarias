archivo = open('archivos//texto.txt')
# para leer el archivo
#print(archivo.read())

# como leer una linea especifica
# va a retornar un arreglo con lineas
# no se puede leer el archivo dos veces, read, readlines
lineas = archivo.readline()
print(lineas)
# cerrar archivo

archivo.close()
# si los archivos son muy grandes no usar readlines