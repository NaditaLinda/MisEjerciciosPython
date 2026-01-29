from functools import reduce

# Datos de entrada: (Fecha, Temp Media, Viento km/h, Lluvia mm)
registros = [
    {"fecha": "2024-01-10", "temp": 12, "viento": 55, "lluvia": 30},
    {"fecha": "2024-01-11", "temp": 14, "viento": 20, "lluvia": 5},
    {"fecha": "2024-01-12", "temp": 9, "viento": 65, "lluvia": 45},
    {"fecha": "2024-01-13", "temp": 18, "viento": 15, "lluvia": 0},
    {"fecha": "2024-01-14", "temp": 10, "viento": 45, "lluvia": 25}
]

# Definición de la condición (Filtro)
# Criterio: Viento > 40 Y Lluvia > 20 Y Temp < 15
es_temporal = lambda r: r["viento"] > 40 and r["lluvia"] > 20 and r["temp"] < 15

# Encadenamiento (Pipeline)
# Con FILTER selecciono los días de temporal
# Con MAP extraigo la cantidad de lluvia de esos días
# Con REDUCE sumo el total de lluvia caída durante todos los temporales detectados

temporales = list(filter(es_temporal, registros))
lluvia_total_temporales = reduce(lambda acumulado, actual: acumulado + actual["lluvia"], temporales, 0)

# Visualización
print(f"Días de temporal detectados: {len(temporales)}")
for t in temporales:
    print(f"- {t['fecha']}: Viento {t['viento']}km/h, Lluvia {t['lluvia']}mm")
print(f"Agregación (Reduce) -> Lluvia total acumulada en temporales: {lluvia_total_temporales}mm")