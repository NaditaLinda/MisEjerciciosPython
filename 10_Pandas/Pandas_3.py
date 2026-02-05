# Escribir una función que reciba un diccionario con las notas de los alumnos
# de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas
# de mayor a menor.

import pandas as pd

def notas_aprobadas_ordenadas(notas):
    serie_notas = pd.Series(notas)
    aprobados = serie_notas[serie_notas >= 5]
    aprobados_ordenados = aprobados.sort_values(ascending=False)
    return aprobados_ordenados

# Ejemplo de uso:
diccionario_notas = {"Ana": 8.5, "Luis": 4.0, "Marta": 9.2, "Juan": 3.5, "Carla": 7.0}
print(notas_aprobadas_ordenadas(diccionario_notas))