import pandas as pd
import csv

df = pd.read_csv('archivos//archivo.csv')
#print(df)

# cambiar el tipo de dato
df['edad'] = df['Edad'].astype(str)


# eliminar filas con datos faltantes
df = df.dropna()
#print(df)

#eliminar filas reepetidas
datos = df.drop_duplicates()
#print(df)


# creacdo un archivo nuevo de cvs apartir de un df
df.to_csv('archivos_problemas_resultos//datos.csv')