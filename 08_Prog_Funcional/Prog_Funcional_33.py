from functools import reduce

# Datos: Erosión medida en cm durante una semana
erosion_diaria = [0.2, 0.5, 0.1, 1.2, 0.4, 0.8, 0.3]

# Factor de progresión
# Cada nuevo evento erosivo impacta un 3% más debido a la debilidad acumulada
FACTOR_PROGRESIVO = 1.03

# Cálculo del impacto total (Reduce + Lambda)
# acc: acumulador del impacto total
# x: valor de erosión del día actual
impacto_final = reduce(lambda acc, x: (acc + x) * FACTOR_PROGRESIVO, erosion_diaria, 0)

# Visualización
print(f"Registros de erosión: {erosion_diaria}")
print(f"Impacto erosivo total corregido: {round(impacto_final, 3)} unidades de impacto")