# Datos de entrada (Listas paralelas)
ids_lobos = ["L-01", "L-02", "L-03", "L-04", "L-05"]
distancias_km = [12.5, 34.2, 8.1, 45.0, 22.8]

# Umbral de actividad (ej: 25 km diarios)
UMBRAL_ACTIVIDAD = 25.0

# Asociación y Filtrado
# zip crea: [("L-01", 12.5), ("L-02", 34.2), ...]
lobos_activos = list(filter(lambda x: x[1] > UMBRAL_ACTIVIDAD, zip(ids_lobos, distancias_km)))

# Visualización de resultados
print(f"Wolves exceeding {UMBRAL_ACTIVIDAD} km today:")
for lobo, dist in lobos_activos:
    print(f"ID: {lobo} | Recorrido: {dist} km")