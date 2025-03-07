# reescribir el archivo se usa, 'w'
# with open('archivos//texto.txt', 'w',encoding='UTF-8') as archivo:
#     # reescribir el arcivo
#     #archivo.write('nyc 2025 wuwu')
#     archivo.writelines(['hola soy mariela\n', 'hola soy popo'])
#     # hola soy mariela hola soy popo


# con append 'a' segun las veces que se ejecute 
with open('archivos//texto.txt', 'a',encoding='UTF-8') as archivo:
    # agregarlo al archivo la cantidad de veces que se ejecute el programa
    archivo.write('hooola')