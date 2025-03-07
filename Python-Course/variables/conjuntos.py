conjunto = set()
conjunto = {1,2,3,4}

# como meter un conjuento dentro de otro conjunto
conjunto1 = frozenset(['hola', 'adios'])
conjunto2  = {conjunto1, 'hasta luego'}
print(conjunto2)

# conjunto a
# a = {1,2,4,6}
#conjunto b -> subconjunto de a 
# b = {2,4,6}

# Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# conjunto 2 es un subconjunto de conjunto 1
resultado = conjunto2.issubset(conjunto1)

# otra manera de comprobar lo mismo
resultado = conjunto2 <= conjunto1


# verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
# va a ser true solo si no tienen ningun numero en comun
print(resultado)