def calcular_cuadrados(muestra):
    """
    Recibe una lista de números y devuelve una nueva lista con sus cuadrados.
    """
    # Creo una lista vacía para guardar los resultados
    cuadrados = []
    
    # Repaso la lista original elemento por elemento
    for numero in muestra:
        # Calculo el cuadrado y lo añado a la nueva lista
        cuadrados.append(numero ** 2)
        
    # Lista final
    return cuadrados

# Ejemplo de uso:
mis_numeros = [2, 4, 6, 8]
resultado = calcular_cuadrados(mis_numeros)
print(f"Original: {mis_numeros}")
print(f"Cuadrados: {resultado}")