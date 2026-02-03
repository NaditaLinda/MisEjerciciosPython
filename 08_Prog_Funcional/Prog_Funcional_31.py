# Datos de entrada (Listas paralelas)
tramos_rios = ["Miño-Ourense", "Sil-Ribas de Sil", "Ulla-Gundián", "Tambre-Sigüeiro"]
caudales = [410.5, 195.2, 82.3, 55.8] # Medido en m³/s

# Definición del umbral de "Alto Caudal"
UMBRAL_CAUDAL = 150.0

# Procesamiento: Combinación y Filtrado
# zip: Sincroniza el tramo con su caudal -> ("Miño-Ourense", 410.5)
# filter + lambda: Evalúa si el segundo elemento (índice 1) supera el umbral
tramos_top = list(filter(lambda x: x[1] > UMBRAL_CAUDAL, zip(tramos_rios, caudales)))

# Presentación de resultados
print(f"Tramos de alto caudal (> {UMBRAL_CAUDAL} m³/s):")
for nombre, valor in tramos_top:
    print(f"• {nombre}: {valor} m³/s")