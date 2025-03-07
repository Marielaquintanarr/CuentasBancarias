# numero mas grande -> max
# numero menor -> min
# round redondear round(numero, a cuantos decimales)
# retorna False -> 0, vacio, False, ninguno
# bool(parametro)
# retorna True si todos los valores son verdaderos
# all(234, 'true')

# parametro args
# forma no optima de sumar lista
# def suma(a,b):
#     return a + b
# tmbn ingresar una lista e irla sumano no es optimo
# forma optima
# el * va a hacer que todos los parametros sean uno
# def sumar(nombre, *numeros):
#     return f'{nombre} la suma es {sum(numeros)}'

# resultado = sumar('Mariela', 2,3,4,5,1)
# print(resultado)

#funciones lambda
# multiplicar por dos
# multiplicar = lambda x : x*2
# print(multiplicar(7))

# usando filter, crea una lista donde todos los valores sean true
numeros = [3,4,25,6,7,89]
def es_par(num):
    if num%2==0:
        return True
    
numeros_pares = filter(es_par, numeros)
num_pares = filter(lambda x : x % 2 == 0, numeros)
#lo tenemos que convertir en una lista
print(list(num_pares))