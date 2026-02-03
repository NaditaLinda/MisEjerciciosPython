from functools import reduce

# Datos: Mediciones de salinidad
# Tomadas en un punto fijo de la ría en distintos estados de marea
salinidad = [35.2, 34.8, 35.5, 36.1, 35.0, 34.5]

# Lógica de Reducción con Memoria de Estado
# state: (valor_anterior, variabilidad_acumulada)
# current: el valor de la nueva medición
# Retorna: (current, variabilidad_acumulada + |current - valor_anterior|)
calc_variabilidad = lambda state, current: (
    current, 
    state[1] + abs(current - state[0])
)

# Ejecución
# Inicializamos con (primer_elemento, 0) y procesamos el resto de la lista
estado_inicial = (salinidad[0], 0)
resultado_final = reduce(calc_variabilidad, salinidad[1:], estado_inicial)

indice_variabilidad = round(resultado_final[1], 2)

print(f"Serie de salinidad: {salinidad}")
print(f"Índice de variabilidad acumulada: {indice_variabilidad}")