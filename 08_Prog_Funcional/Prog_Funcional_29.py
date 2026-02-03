# Datos de entrada (Listas paralelas por estación/día)
temperaturas = [12.5, 8.2, 7.5, 14.0, 9.1]
precipitaciones = [5.0, 22.4, 18.2, 2.1, 35.0]

# Condición compuesta: "Temporal Frío"
# Umbral: Temperatura < 10°C Y Precipitación > 15mm
es_temporal_frio = lambda x: x[0] < 10 and x[1] > 15

# Combinación y Filtrado
# zip une: (12.5, 5.0), (8.2, 22.4)...
registros_filtrados = list(filter(es_temporal_frio, zip(temperaturas, precipitaciones)))

# Resultados
print(f"Se han detectado {len(registros_filtrados)} registros de temporal frío:")
for t, p in registros_filtrados:
    print(f"- Temp: {t}°C | Lluvia: {p}mm")