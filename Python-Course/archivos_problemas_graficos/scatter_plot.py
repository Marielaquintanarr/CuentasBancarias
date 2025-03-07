import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_resultos//datos.csv')
#sns.barplot(x='Nombre', y = 'Edad', data = df)

# dispersion
sns.boxplot(x='Edad', y = 'Edad', data = df)
#total_edad = df['Edad'].sum()
#print(total_edad)
plt.show()