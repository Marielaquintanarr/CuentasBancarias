# listas
nombres = ['Mariela', 'Sofia', 'Tamara']
apellidos = ['quintanar', 'de la mora', 'benavides']

with open('nombres_y_apellidos.txt', 'w') as archivo:
    archivo.writelines('los datos son: \n')
    [archivo.writelines(f'Nombre: {n} \nApellido: {a}\n') for n, a in zip(nombres, apellidos)]


