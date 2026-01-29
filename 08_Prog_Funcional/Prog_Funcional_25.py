# Datos de entrada: Temperatura (°C), Oxigeno (mg/L) y Obstáculos (Boolean)
rios_gallegos = [
    {"nombre": "Eo", "temp": 14, "oxigeno": 9.5, "obstaculos": False},
    {"nombre": "Miño", "temp": 19, "oxigeno": 7.2, "obstaculos": True},
    {"nombre": "Ulla", "temp": 15, "oxigeno": 8.8, "obstaculos": False},
    {"nombre": "Lérez", "temp": 16, "oxigeno": 6.5, "obstaculos": False},
    {"nombre": "Eume", "temp": 13, "oxigeno": 9.1, "obstaculos": False}
]

# Definición del criterio de idoneidad (Lambda)
# El salmón requiere: Temp < 17°C, Oxígeno > 8mg/L y SIN obstáculos
es_apto_salmon = lambda r: r["temp"] < 17 and \
                           r["oxigeno"] > 8 and \
                           not r["obstaculos"]

# Filtrado de la lista
rios_reproduccion = list(filter(es_apto_salmon, rios_gallegos))

# Visualización de resultados
print("Ríos aptos para la reproducción del salmón:")
for rio in rios_reproduccion:
    print(f"-> {rio['nombre']}: Condición óptima detectada.")