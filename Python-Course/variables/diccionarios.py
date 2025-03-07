# creando diccionario
# las tuplas pueden se claves, pero las listas no conjuntos que no sean frozenset no porque no son hasheables
diccionario = dict(nombre = 'Mariela', apellido = 'Quintanar')

diccionario = {
    'nombre' : 'Mariela',
    'apellido' : 'Quintaar'

}


diccionario = dict.fromkeys('nombre', 'apellido')
# {'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido'}

# para evitar esto se pone una lista en el primer elemento
diccionario = dict.fromkeys(['quintanar', 'rios', 'gomez'], 'apellido')
print(diccionario)
#{'quintanar': 'apellido', 'rios': 'apellido', 'gomez': 'apellido'}