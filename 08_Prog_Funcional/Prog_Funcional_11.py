import math

def obtener_valores_atipicos(muestra):
    """
    Identifica los valores de una lista con una puntuación típica mayor a 3 o menor a -3.
    """
    if len(muestra) < 2:
        return []

    # Calcular la media (μ)
    media = sum(muestra) / len(muestra)
    
    # Calcular la desviación típica (σ)
    varianza = sum((x - media) ** 2 for x in muestra) / len(muestra)
    desviacion_tipica = math.sqrt(varianza)
    
    # Si la desviación es 0, todos los números son iguales y no hay atípicos
    if desviacion_tipica == 0:
        return []

    # Filtrar valores con puntuación típica |z| > 3
    atipicos = []
    for x in muestra:
        # Puntuación típica: z = (x - media) / desviacion_tipica
        z_score = (x - media) / desviacion_tipica
        
        if z_score > 3 or z_score < -3:
            atipicos.append(x)
            
    return atipicos

# Ejemplo de uso con una muestra que tiene un valor muy alejado (100)
datos = [10, 12, 11, 13, 12, 11, 10, 100]
print(f"Valores atípicos encontrados: {obtener_valores_atipicos(datos)}")