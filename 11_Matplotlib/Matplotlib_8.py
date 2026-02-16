"""
El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Crear un dataframe con Pandas y a partir de él generar los siguientes diagramas.

Diagrama de sectores con los fallecidos y supervivientes.
Histograma con las edades.
Diagrama de barras con el número de personas en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes en cada clase.
Diagrama de barras con el número de personas fallecidas y supervivientes acumuladas en cada clase.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('titanic.csv')

# Diagrama 1: Sectores (Fallecidos vs. Supervivientes)
conteo_supervivientes=df['Survived'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(conteo_supervivientes, labels=['Fallecidos', 'Supervivientes'], autopct='%1.2f%%', colors=['#ff9999', '#66b3ff'])
plt.title('Distribución de fallecidos y supervivientes')
plt.savefig('titanic_sectores.png')

# Diagrama 2: Histograma (Edades)
plt.figure(figsize=(8, 6))
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de edades de los pasajeros')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.savefig('titanic_histograma.png')

# Diagrama 3: Barra (Personas por clase)
personas_clase=df['Pclass'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
personas_clase.plot(kind='bar', color='teal')
plt.title('Pasajeros por clase')
plt.xlabel('Clase')
plt.ylabel('Número de personas')
plt.xticks(rotation=0)
plt.savefig('titanic_barras_clase.png')

# Diagrama 4: Barra (Fallecidos y supervivientes por clase)
tabla_clase = pd.crosstab(df['Pclass'], df['Survived'])
tabla_clase.columns = ['Fallecidos', 'Supervivientes']

plt.figure(figsize=(8, 6))
tabla_clase.plot(kind='bar', ax=plt.gca(), color=['#ff9999', '#66b3ff'])
plt.title('Fallecidos y supervivientes por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.legend(title='Estado')
plt.xticks(rotation=0)
plt.savefig('titanic_barras_comparativo.png')

# Diagrama 5: Barra acumulada (Apiladas)
plt.figure(figsize=(8, 6))
tabla_clase.plot(kind='bar', stacked=True, ax=plt.gca(), color=['#ff9999', '#66b3ff'])
plt.title('Fallecidos y supervivientes acumulados por clase')
plt.xlabel('Clase')
plt.ylabel('Cantidad')
plt.legend(title='Estado')
plt.xticks(rotation=0)
plt.savefig('titanic_barras_acumuladas.png')
