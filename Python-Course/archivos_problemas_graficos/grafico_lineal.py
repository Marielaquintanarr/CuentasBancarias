import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_resultos//datos.csv')
sns.lineplot(x='Nombre', y = 'Edad', data = df)
plt.show()