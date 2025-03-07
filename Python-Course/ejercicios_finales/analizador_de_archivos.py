'''
### 2. **Analizador de Texto (Archivos TXT + Estructuras de Datos)**  
**Descripción:**  
Desarrolla un programa que lea un archivo de texto y analice la frecuencia de las palabras.

**Requisitos:**  
- Lee un archivo `.txt` dado por el usuario.
- Usa un diccionario para contar cuántas veces aparece cada palabra.
- Muestra las 5 palabras más comunes con su frecuencia.

'''
import re
class Archivo:
    def __init__(self):
        self.diccionario = {}

    def crear_archivo(self):
        nombre = input('Ingresa el nombre del archivo: ')
        contenido = input('Ingresa el contenido del archivo: ')
        with open(f'ejercicios_finales//{nombre}.txt', 'w') as archivo:
            archivo.writelines(contenido)

    def contar_palabras(self):
        nombre_archivo = input('Ingresa el nombre del archivo sin .txt: ')
        palabra = input('Ingresa la palabra a buscar: ').lower()
        with open(f'ejercicios_finales//{nombre_archivo}.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read().lower()
        
        lista = re.findall(r'\b\w+\b', texto)
        
        for p in lista:
            if p in self.diccionario:
                self.diccionario[p] += 1
            else:
                self.diccionario[p] = 1
        
        print(f'La palabra: {palabra} se encontro {self.diccionario[palabra]} veces')

    def contar_5_top_palabras(self):
        nombre_archivo = input('Ingresa el nombre del archivo sin .txt: ')
        with open(f'ejercicios_finales//{nombre_archivo}.txt', 'r', encoding='utf-8') as archivo:
            texto = archivo.read().lower()
        
        lista = re.findall(r'\b\w+\b', texto)
        
        for p in lista:
            if p in self.diccionario:
                self.diccionario[p] += 1
            else:
                self.diccionario[p] = 1

        ordenado = sorted(self.diccionario.items(), key=lambda item: item[1], reverse=True)


        print(ordenado[:5])

    
archivo = Archivo()
archivo.crear_archivo()
archivo.contar_5_top_palabras()


