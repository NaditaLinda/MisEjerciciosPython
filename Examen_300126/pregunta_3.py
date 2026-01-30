import pandas as pd
import os

# Bloque de carga (Necesario en cada nuevo script)
base_path = os.path.dirname(__file__)

# Cargamos los DataFrames necesarios para esta pregunta
df_fincas = pd.read_csv(os.path.join(base_path, 'fincas.csv'))
df_propietarios = pd.read_csv(os.path.join(base_path, 'propietarios.csv'))
# También cargamos titularidad por si quieres probar el ejemplo de uso
df_titul = pd.read_csv(os.path.join(base_path, 'titularidad.csv'))

# Diccionario de Fincas: {id_finca: fila_completa}
finca_por_id = df_fincas.set_index('id_finca').to_dict('index')

# Diccionario de Propietarios: {id_propietario: nombre}
propietario_por_id = df_propietarios.set_index('id_propietario')['nombre_completo'].to_dict()

print("✅ Diccionarios creados correctamente.")

# --- Ejemplo de prueba para verificar que funciona ---
print(f"Nombre del propietario 501: {propietario_por_id.get(501)}")