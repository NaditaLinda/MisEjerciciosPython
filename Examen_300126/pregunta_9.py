import pandas as pd
import os

# Preparación de datos (Rutas robustas)
base_path = os.path.dirname(__file__)
df_fincas = pd.read_csv(os.path.join(base_path, 'fincas.csv'))
df_propietarios = pd.read_csv(os.path.join(base_path, 'propietarios.csv'))
df_titul = pd.read_csv(os.path.join(base_path, 'titularidad.csv'))

# Creación de diccionarios de consulta rápida
fincas_superficie = df_fincas.set_index('id_finca')['superficie_m2'].to_dict()
nombres_propietarios = df_propietarios.set_index('id_propietario')['nombre_completo'].to_dict()

# Diccionario para acumular estadísticas {id_propietario: {datos}}
stats = {}

# Procesamiento de la titularidad
for _, fila in df_titul.iterrows():
    id_p = fila['id_propietario']
    id_f = fila['id_finca']
    porcentaje = fila['porcentaje_propiedad']
    
    # Obtenemos la superficie de la finca desde nuestro mapa
    superficie_finca = fincas_superficie.get(id_f, 0)
    
    # Cálculo de superficie ponderada (Lo que realmente posee la persona)
    superficie_ponderada = (porcentaje / 100) * superficie_finca
    
    # Inicializamos el registro del propietario si no existe
    if id_p not in stats:
        stats[id_p] = {
            'nombre': nombres_propietarios.get(id_p, "Desconocido"),
            'num_fincas': 0,
            'superficie_total_m2': 0.0
        }
    
    # Acumulamos los valores
    stats[id_p]['num_fincas'] += 1
    stats[id_p]['superficie_total_m2'] += superficie_ponderada

# Conversión a DataFrame para el Ranking final
df_ranking = pd.DataFrame.from_dict(stats, orient='index')

# Ordenamos de mayor a menor superficie total
df_final = df_ranking.sort_values(by='superficie_total_m2', ascending=False)

# Salida por pantalla
print("--- RANKING DE PROPIETARIOS POR CONTROL DE SUPERFICIE ---")
print(df_final.to_string(index=False))