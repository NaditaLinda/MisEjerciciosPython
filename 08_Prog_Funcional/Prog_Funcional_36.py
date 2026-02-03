from functools import reduce

# Datos: Extracciones diarias en kg (Lunes a Viernes)
extracciones = [120, 85, 150, 60, 200]

# Factor de impacto acumulativo (ej: cada paso incrementa el peso del impacto un 2%)
FACTOR_ESTRES = 1.02

# Lógica de Reducción (Lambda)
# acc: impacto acumulado hasta el momento
# x: extracción del día actual
logica_impacto = lambda acc, x: (acc + x) * FACTOR_ESTRES

# Ejecución del proceso
# El 0 inicial es el punto de partida del acumulador
impacto_total = reduce(logica_impacto, extracciones, 0)

print(f"Historial de extracciones: {extracciones} kg")
print(f"Valor de impacto total calculado: {round(impacto_total, 2)}")