import pandas as pd
import os

# Preparación y carga
base_path = os.path.dirname(__file__)
ruta_fincas = os.path.join(base_path, 'fincas.csv')
df_fincas = pd.read_csv(ruta_fincas)

# Selección de las columnas solicitadas
columnas_listado = ['direccion', 'municipio', 'uso', 'superficie_m2']
df_listado = df_fincas[columnas_listado]

# Ordenación de mayor a menor superficie

df_ordenado = df_listado.sort_values(by='superficie_m2', ascending=False)

# Resultado
print("--- LISTADO OPERATIVO DE FINCAS (Ordenado por superficie) ---")
print(df_ordenado.to_string(index=False))

# Opcional: Guardar este informe específico
# df_ordenado.to_csv(os.path.join(base_path, 'Informe_Fincas_Superficie.csv'), index=False)