import pandas as pd

# Generar un DataFrame con los datos del fichero
try:
    df = pd.read_csv('titanic.csv')
    print("Archivo cargado con éxito.\n")
except FileNotFoundError:
    print("Error: El archivo 'titanic.csv' no se encuentra en la carpeta.")
    exit()

# Mostrar dimensiones, número de datos, nombres de columnas/filas, tipos, 10 primeras y 10 últimas
print("--- Información General ---")
print(f"Dimensiones (filas, columnas): {df.shape}")
print(f"Número total de datos (celdas): {df.size}")
print(f"Nombres de columnas: {df.columns.tolist()}")
print(f"Nombres de filas (índice): {df.index}")
print("\nTipos de datos de las columnas:")
print(df.dtypes)
print("\n10 Primeras filas:")
print(df.head(10))
print("\n10 Últimas filas:")
print(df.tail(10))

# Mostrar los datos del pasajero con identificador 148
# Buscamos en la columna 'PassengerId'
print("\n--- Pasajero con ID 148 ---")
print(df[df['PassengerId'] == 148])

# Mostrar las filas pares
# Usamos iloc con un salto de 2 empezando desde 0
print("\n--- Filas pares del DataFrame ---")
print(df.iloc[::2])

# Nombres de personas en primera clase ordenadas alfabéticamente
print("\n--- Pasajeros de 1ª Clase (Orden Alfabético) ---")
primera_clase_nombres = df[df['Pclass'] == 1]['Name'].sort_values()
print(primera_clase_nombres)

# Porcentaje de personas que sobrevivieron y murieron
print("\n--- Porcentaje de supervivencia total ---")
# normalize=True devuelve la proporción, multiplicamos por 100 para porcentaje
supervivencia = df['Survived'].value_counts(normalize=True) * 100
print(f"Murió (0): {supervivencia[0]:.2f}%")
print(f"Sobrevivió (1): {supervivencia[1]:.2f}%")

# Porcentaje de personas que sobrevivieron en cada clase
print("\n--- Supervivencia por Clase ---")
supervivencia_clase = df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100
print(supervivencia_clase)

# Eliminar pasajeros con edad desconocida (NaN)
df = df.dropna(subset=['Age'])
print(f"\nDataFrame actualizado: Se han eliminado las filas con edad desconocida.")

# Edad media de las mujeres que viajaban en cada clase
print("\n--- Edad media de mujeres por clase ---")
media_edad_mujeres = df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
print(media_edad_mujeres)

# Añadir nueva columna booleana para menores de edad (menor de 18 años)
df['EsMenor'] = df['Age'] < 18
print("\nColumna 'EsMenor' añadida correctamente.")

# Porcentaje de menores y mayores de edad que sobrevivieron en cada clase
print("\n--- Supervivencia de Menores vs Mayores por Clase ---")
# Agrupamos por Clase y por la nueva columna booleana
supervivencia_edad_clase = df.groupby(['Pclass', 'EsMenor'])['Survived'].value_counts(normalize=True) * 100
print(supervivencia_edad_clase)