import pandas as pd
import os

# Ruta de la carpeta donde está el script ---
ruta_script = os.path.dirname(__file__)

# Definición de los esquemas para cada archivo csv
esquemas = {
    "fincas.csv": ["id_finca", "referencia_catastral", "tipo_inmueble", "direccion", "municipio", "provincia", "superficie_m2", "uso"],
    "propietarios.csv": ["id_propietario", "nombre_completo", "dni", "direccion_contacto"],
    "titularidad.csv": ["id_titularidad", "id_finca", "id_propietario", "porcentaje_propiedad"],
    "cargas.csv": ["id_carga", "id_finca", "tipo_carga", "descripcion", "fecha_inscripcion"],
    "inscripciones.csv": ["id_inscripcion", "id_finca", "tipo_inscripcion", "fecha", "observaciones"]
}

dataframes = {}

print("--- INICIANDO VALIDACIÓN DE DATOS ---")

for archivo, columnas_esperadas in esquemas.items():
    ruta_completa = os.path.join(ruta_script, archivo)
    
    try:
        if os.path.exists(ruta_completa):
            df = pd.read_csv(ruta_completa)

            columnas_reales = list(df.columns)
            
            # Comprobación de columnas para verificar si están todas las esperadas
            faltan = [col for col in columnas_esperadas if col not in columnas_reales]
            
            if not faltan:
                print(f"✅ {archivo}: Cargado correctamente.")
                print(f"   -> Registros encontrados: {len(df)}")
                dataframes[archivo] = df
            else:
                print(f"❌ ERROR en {archivo}: Faltan las columnas: {faltan}")
        else:
            print(f"⚠️ AVISO: El archivo '{archivo}' no se encuentra en la carpeta actual.")
            
    except Exception as e:
        print(f"🚨 Error inesperado al procesar {archivo}: {e}")

print("--- PROCESO FINALIZADO ---")       