# ejercicio 2
texto = input('Ingresa el texto: ')
texto_separado = texto.split(' ')
total_palabras = len(texto_separado)
total_segundos = len(texto_separado) / 2

if total_segundos > 60:
    print('no tanto')

treinta_por_ciento_mas_rapido = total_palabras/2*1.3
print(treinta_por_ciento_mas_rapido)

