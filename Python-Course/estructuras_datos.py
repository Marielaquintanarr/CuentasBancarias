#tuplas

tupla = ('Hola', 23, 78.7)
lista = ['Hola', 23, 78.7]

# la tupla no se puede modificar
#tupla[0] = 'mariela'

# conjuntos

# no podemos acceder a cada elemento por el indice
conjunto = {'hola', 2, 3}

diccionario = {
    'nombre' : 'mariela',
    'edad' : 20,
    'altura' : 1.63
}



# mayuscm minus, caps
cadena = 'Mariela quintanar de La Mora'

busqueda = cadena.find('h')
# regresa el indice de la primera a, si no lo encuentra -1
#print(busqueda)

# regresa el indice
busqueda = cadena.index('a')

es_numerico = cadena.isnumeric()

es_alphanum= cadena.isalpha()


contar_coincidencias = cadena.count('a')

empieza_con = cadena.startswith('Mariela')

termina_con = cadena.endswith('Mariela')

# remplazar_pedazo_de_cadena
remplazar = cadena.replace('a', 'o')

separar = cadena.split('a')
print(separar)