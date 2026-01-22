def calcular_media(muestra):
    """
    Calcula la media aritmética de una lista de números.
    """
    if not muestra:  # Verificamos si la lista está vacía
        return 0
    
    suma_total = sum(muestra)
    total_elementos = len(muestra)
    
    media = suma_total / total_elementos
    return media

# Ejemplo de uso:
numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print(f"La media de la muestra es: {resultado}")