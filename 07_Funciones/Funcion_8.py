import math

def calcular_estadisticas(muestra):
    """
    Calcula la media, varianza y desviación típica de una lista de números.
    """
    if not muestra:
        return {"media": 0, "varianza": 0, "desviacion_tipica": 0}

    n = len(muestra)
    
    # Calcular la Media
    media = sum(muestra) / n
    
    # Calcular la Varianza
    # Suma de los cuadrados de las diferencias respecto a la media
    suma_varianza = sum((x - media) ** 2 for x in muestra)
    varianza = suma_varianza / n
    
    # Calcular la Desviación Típica
    desviacion = math.sqrt(varianza)
    
    # Retornar el Diccionario
    return {
        "media": media,
        "varianza": varianza,
        "desviacion_tipica": desviacion
    }

# Ejemplo de uso:
datos = [10, 12, 23, 23, 16, 23, 21, 16]
resultado = calcular_estadisticas(datos)

print("📊 Reporte Estadístico:")
for clave, valor in resultado.items():
    print(f"{clave.replace('_', ' ').capitalize()}: {valor:.2f}")