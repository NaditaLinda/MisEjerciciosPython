import pandas as pd

def calcular_estadisticas_notas(notas):
    # Transformación: Convertimos el diccionario en una Serie de Pandas
    serie_notas = pd.Series(notas)

    # Computación: Creamos una nueva Serie con los resultados estadísticos
    estadisticas = pd.Series({
        'Mínima': serie_notas.min(),
        'Máxima': serie_notas.max(),
        'Media': serie_notas.mean(),
        'Desviación típica': serie_notas.std()
    })

    return estadisticas

# Ejemplo de uso:
notas_clase = {
    'Ana': 9.5, 
    'Luis': 4.0, 
    'Marta': 7.5, 
    'Juan': 6.0, 
    'Elena': 8.2
}

resultado = calcular_estadisticas_notas(notas_clase)
print(resultado)