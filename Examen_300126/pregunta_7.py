import pandas as pd
import os

# Carga de datos
base_path = os.path.dirname(__file__)
df_cargas = pd.read_csv(os.path.join(base_path, 'cargas.csv'))

# Seleccionamos las fincas que tienen gravámenes reales
df_solo_gravamenes = df_cargas[df_cargas['tipo_carga'] != 'Libre de cargas'].copy()

# Cálculo de fincas distintas afectadas usndo nunique()
total_afectadas = df_solo_gravamenes['id_finca'].nunique()

# Generación del listado solicitado
listado_legal = df_solo_gravamenes[['id_finca', 'tipo_carga']].sort_values(by='id_finca')

# Salida por pantalla
print(f"--- INFORME PARA DEPARTAMENTO LEGAL ---")
print(f"Total de fincas distintas afectadas por cargas: {total_afectadas}")
print("-" * 40)
print("Detalle de cargas por finca:")
print(listado_legal.to_string(index=False))