import pandas as pd

# df -> dataframe (es como una hoja de calculo)
df = pd.read_csv('archivos//archivo.csv')
df2 = pd.read_csv('archivos//archivo.csv')
nombres = df['Nombre']

# ordenar df por edad
df_ordenado = df.sort_values('Edad')
#print(df_ordenado)

# de forma descendente
df_ordenado_descendente = df.sort_values('Edad', ascending=False)
#print(df_ordenado_descendente)

# concatenar
df_concatenado = pd.concat([df, df2])
#print(df_concatenado)

# acceder a la primer fila : head
primer_fila = df.head(1)
#print(primer_fila)

# accediendo a las ultimas filas
ultimas_filas = df.tail(1)
#print(ultimas_filas)

# accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape
#print(columnas_totales)

# obteniendo data estadistica
df_info = df.describe()
#print(df_info)

# accediendo a un elemento especifico con loc
elemento = df.loc[2, 'Nombre']
#print(elemento)

# accediendo al nombre (columna 1), de la fila 2
elemento = df.iloc[2, 1]
#print(elemento)


# accediendo a todas las filas de una columna
apellidos = df.iloc[:, 1]
print(apellidos)