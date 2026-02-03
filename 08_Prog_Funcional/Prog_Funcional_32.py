from functools import reduce

# Datos de entrada: Precipitaciones diarias en mm
precipitaciones = [12.5, 45.0, 8.2, 60.5, 15.0, 5.2]

# Configuración del índice
UMBRAL_EXTREMO = 40.0
FACTOR_PENALIZACION = 1.5

# Lógica de acumulación con penalización (Lambda)
# acc: acumulador (el total parcial)
# p: precipitación actual de la lista
fórmula_indice = lambda acc, p: acc + (p * FACTOR_PENALIZACION if p > UMBRAL_EXTREMO else p)

# Ejecución de la reducción
# El 0 final es el valor inicial del acumulador (acc)
indice_acumulado = reduce(fórmula_indice, precipitaciones, 0)

# Visualización
print(f"Lista de precipitaciones: {precipitaciones}")
print(f"Índice de lluvia acumulada (penalizada): {round(indice_acumulado, 2)}")