# Datos: Humedad (%) y Visibilidad (metros)
registros_meteo = [
    {"fecha": "2026-01-20", "humedad": 98, "visibilidad": 80},
    {"fecha": "2026-01-21", "humedad": 70, "visibilidad": 5000},
    {"fecha": "2026-01-22", "humedad": 95, "visibilidad": 120},
    {"fecha": "2026-01-23", "humedad": 92, "visibilidad": 300},
    {"fecha": "2026-01-24", "humedad": 85, "visibilidad": 1000}
]

# Definición del criterio de "Niebla Densa"
# Condición: Humedad > 90% Y Visibilidad < 200 metros
es_niebla_densa = lambda r: r["humedad"] > 90 and r["visibilidad"] < 200

# Aplicación del filtro
# filter() solo deja pasar los elementos donde la lambda devuelve True
dias_criticos = list(filter(es_niebla_densa, registros_meteo))

# Visualización
print(f"Se han detectado {len(dias_criticos)} días con niebla densa:")
for dia in dias_criticos:
    print(f"- Fecha: {dia['fecha']} | Humedad: {dia['humedad']}% | Visibilidad: {dia['visibilidad']}m")