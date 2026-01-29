# Datos: Temperaturas medias en comarcas del interior (Ourense, Verín, Lugo, etc.)
temps_interior = [4, 12, 18, 25, 34, -2]

# Parámetros de la fórmula
TEMP_CONFORT = 18

# Transformación con map y lambda
# Fórmula: Penalización = (Temperatura - Confort)^2 / 10
# Al elevar al cuadrado, los valores lejanos al 18 crecen exponencialmente.
calcular_indice = lambda t: round(((t - TEMP_CONFORT)**2) / 10, 2)

indices_penalizados = list(map(calcular_indice, temps_interior))

# Resultado
print(f"Temperaturas originales (°C): {temps_interior}")
print(f"Índices de penalización:      {indices_penalizados}")