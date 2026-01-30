import pandas as pd
import os

# Ruta completa del script
base_path = os.path.dirname(__file__)

# Cargo los dataframes
df_fincas = pd.read_csv(os.path.join(base_path, 'fincas.csv'))
df_titul = pd.read_csv(os.path.join(base_path, 'titularidad.csv'))
df_propietarios = pd.read_csv(os.path.join(base_path, 'propietarios.csv'))
df_cargas = pd.read_csv(os.path.join(base_path, 'cargas.csv'))
df_inscrip = pd.read_csv(os.path.join(base_path, 'inscripciones.csv'))

print("✅ Todos los archivos han sido cargados con éxito usando rutas absolutas.")

def limpiar_dataframe(df):
    # Elimino espacios extra en todas las columnas de texto
    columnas_texto = df.select_dtypes(include=['object', 'str']).columns
    for col in columnas_texto:
        df[col] = df[col].astype(str).str.strip()
    return df

# Aplicamos limpieza de texto a todos
df_fincas = limpiar_dataframe(df_fincas)
df_titul = limpiar_dataframe(df_titul)
df_cargas = limpiar_dataframe(df_cargas)
df_inscrip = limpiar_dataframe(df_inscrip)
df_propietarios = limpiar_dataframe(df_propietarios)

# Conversión de fechas (Si falla se marca como NaT con coerce).
df_cargas['fecha_inscripcion'] = pd.to_datetime(df_cargas['fecha_inscripcion'], errors='coerce')
df_inscrip['fecha'] = pd.to_datetime(df_inscrip['fecha'], errors='coerce')

# Aseguramos tipos numéricos (coerce convierte errores en NaN)
df_fincas['superficie_m2'] = pd.to_numeric(df_fincas['superficie_m2'], errors='coerce')
df_titul['porcentaje_propiedad'] = pd.to_numeric(df_titul['porcentaje_propiedad'], errors='coerce')

# Detección de registros sospechosos
print("--- AUDITORÍA DE CALIDAD DE DATOS ---")

# Sospechosos en Fincas (Superficie <= 0)
fincas_error = df_fincas[df_fincas['superficie_m2'] <= 0]
if not fincas_error.empty:
    print(f"⚠️ Alerta: Se han encontrado {len(fincas_error)} fincas con superficie errónea.")
else:
    print("✅ Superficies validadas correctamente.")

# Sospechosos en Titularidad (Porcentaje > 100)
titul_error = df_titul[df_titul['porcentaje_propiedad'] > 100]
if not titul_error.empty:
    print(f"⚠️ Alerta: Se han encontrado {len(titul_error)} registros de titularidad superiores al 100%.")
else:
    print("✅ Porcentajes de titularidad dentro del rango legal.")

# Verificación de fechas nulas (NaT)
fechas_mal = df_inscrip['fecha'].isna().sum()
if fechas_mal > 0:
    print(f"⚠️ Hay {fechas_mal} registros con fechas inválidas en Inscripciones.")

print("--- LIMPIEZA COMPLETADA ---")