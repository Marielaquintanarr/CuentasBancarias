import re

texto = '''Hola Mariela, esta es la cadena 1
Adiosss a todoosssnfifj 32 212
odio ir a la escuela'''

# busqueda simple
resultado = re.search('Mariela', texto)
resultado = re.findall('Mariela', texto)
resultado = re.findall('Mariela', texto, flags=re.IGNORECASE)

# \d busca digitos del 0 al 9
resultado = re.findall(r'\d', texto)

# \d busca todo MENOS digitos del 0 al 9
resultado = re.findall(r'\D', texto)

# \w busca alphanumericos
resultado = re.findall(r'\w', texto)

# \W busca todo MENOS alphanumericos
resultado = re.findall(r'\W', texto)

# \s busca espacios en blaco y saltos de linea
resultado = re.findall(r'\s', texto)


# \S busca TODO MENOS espacios en blaco y saltos de linea
resultado = re.findall(r'\S', texto)

# \S busca TODO MENOS saltos de linea
resultado = re.findall(r'\.', texto)

# \S busca TODO saltos de linea
resultado = re.findall(r'\n', texto)

# \ cancela todos los caracteres especiales, cancelando la funcion del punto y buscamdo puntos
resultado = re.findall(r'\.', texto)

# generando cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(f'\d\.\s', texto)

# buscando el comienzo de una linea
resultado = re.findall('^Hols', texto)

# buscando el final de una linea
resultado = re.findall('$Hola', texto)

# buscar una cosa o la otra |
resultado = re.findall(r'\d{2,4} | Hola', texto)