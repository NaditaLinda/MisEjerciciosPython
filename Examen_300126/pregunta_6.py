import pandas as pd
import os

# Carga de datos con ruta absoluta
base_path = os.path.dirname(__file__)
df_titul = pd.read_csv(os.path.join(base_path, 'titularidad.csv'))

# Agrupo y calculo los datos solicitados
resumen_compartidas = df_titul.groupby('id_finca').agg(
    suma_porcentajes=('porcentaje_propiedad', 'sum'),
    numero_propietarios=('id_propietario', 'count')
).reset_index()

# Filtramos para detectar SOLO la titularidad compartida
listado_compartidas = resumen_compartidas[resumen_compartidas['numero_propietarios'] > 1]

# Listado por pantalla
print("--- FINCAS CON TITULARIDAD COMPARTIDA ---")

if listado_compartidas.empty:
    print("No se han encontrado fincas con más de un propietario.")
else:
    # Mostramos las 3 columnas solicitadas
    print(listado_compartidas[['id_finca', 'suma_porcentajes', 'numero_propietarios']].to_string(index=False))

