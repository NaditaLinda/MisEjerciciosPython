def filtrar_lista(condicion, lista):
    """
    Recibe una función booleana y una lista.
    Devuelve una nueva lista con los elementos que cumplen la condición.
    """
    # Inicio la lista de resultados
    resultado = []
    
    # Recorro la lista original
    for elemento in lista:
        # Aplicamos la función booleana al elemento actual
        if condicion(elemento):
            # Si el resultado es True, lo añadimos
            resultado.append(elemento)
            
    # Devuelve la lista filtrada
    return resultado

# --- Ejemplo de uso ---

# Definimos una función booleana sencilla (predicado)
def es_par(n):
    return n % 2 == 0

# Creamos una lista de prueba
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llamo a la función de orden superior
pares = filtrar_lista(es_par, numeros)

print(f"Lista original: {numeros}")
print(f"Elementos que cumplen la condición (pares): {pares}")