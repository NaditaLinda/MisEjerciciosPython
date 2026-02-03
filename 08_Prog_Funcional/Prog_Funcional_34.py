from functools import reduce

# Datos: Producción diaria de 5 aerogeneradores (en MWh)
produccion_mwh = [15.5, 22.0, 18.2, 25.4, 12.8]

# Factor de eficiencia (0.98 representa un 2% de pérdida acumulada)
FACTOR_EFICIENCIA = 0.98

# Lógica de acumulación con pérdidas (Lambda)
# acc: acumulador de la energía total
# x: producción del aerogenerador actual
formula_perdidas = lambda acc, x: (acc + x) * FACTOR_EFICIENCIA

# Cálculo final
# Iniciamos el acumulador en 0
total_ajustado = reduce(formula_perdidas, produccion_mwh, 0)

print(f"Producción bruta total: {sum(produccion_mwh)} MWh")
print(f"Producción ajustada (con pérdidas): {round(total_ajustado, 2)} MWh")