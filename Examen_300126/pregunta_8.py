import pandas as pd
import os

# Preparación de la ruta base para cargar los archivos CSV
base_path = os.path.dirname(__file__)

# Cargamos las dos tablas necesarias
df_inscrip = pd.read_csv(os.path.join(base_path, 'inscripciones.csv'))
df_cargas = pd.read_csv(os.path.join(base_path, 'cargas.csv'))

# Aseguramos que las fechas sean tratadas como objetos de tiempo para poder ordenarlas
df_inscrip['fecha'] = pd.to_datetime(df_inscrip['fecha'])
df_cargas['fecha_inscripcion'] = pd.to_datetime(df_cargas['fecha_inscripcion'])

def historial_finca(id_finca):
    """
    Genera el historial unificado de una finca ordenado por fecha.
    """
    historial = []

    # Recuperar y formatear Inscripciones
    f_inscrip = df_inscrip[df_inscrip['id_finca'] == id_finca]
    for _, fila in f_inscrip.iterrows():
        historial.append({
            "fecha": fila['fecha'],
            "tipo": "Inscripción",
            "descripcion": f"{fila['tipo_inscripcion']}: {fila['observaciones']}"
        })

    # Recuperar y formatear Cargas
    f_cargas = df_cargas[df_cargas['id_finca'] == id_finca]
    for _, fila in f_cargas.iterrows():
        # Quito "Libre de cargas" del historial de afectaciones
        if fila['tipo_carga'] != "Libre de cargas":
            historial.append({
                "fecha": fila['fecha_inscripcion'],
                "tipo": "Carga",
                "descripcion": f"{fila['tipo_carga']}: {fila['descripcion']}"
            })

    # Ordeno por fecha (de más antigua a más reciente) usando una función lambda
    historial_ordenado = sorted(historial, key=lambda x: x['fecha'])

    # Convierto las fechas de nuevo a texto para una lectura más limpia
    for registro in historial_ordenado:
        registro['fecha'] = registro['fecha'].strftime('%Y-%m-%d')

    return historial_ordenado

# --- Ejemplo de uso ---
entrada = input("🏠 Introduce el código de la finca que quieres consultar (Entre 1001 y 1030): ")
id_test = int(entrada)
print(f"--- HISTORIAL JURÍDICO DE LA FINCA {id_test} ---")
for h in historial_finca(id_test):
    print(f"[{h['fecha']}] {h['tipo'].upper()}: {h['descripcion']}")