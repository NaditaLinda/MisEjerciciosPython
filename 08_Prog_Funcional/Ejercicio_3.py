# Defino la función de orden superior
def aplicar_a_lista(funcion_transformadora, lista_entrada):
    # Creo una lista vacía para guardar los resultados
    lista_resultado = []
    
    # Recorro cada elemento de la lista original
    for elemento in lista_entrada:
        # Aplico la función recibida al elemento actual
        nuevo_valor = funcion_transformadora(elemento)
        # Guardo el resultado en una nueva lista
        lista_resultado.append(nuevo_valor)
        
    return lista_resultado

# --- Ejemplos de uso ---

# Ejemplo A: Elevar al cuadrado
def al_cuadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
resultado_cuadrados = aplicar_a_lista(al_cuadrado, numeros)
print(f"Cuadrados: {resultado_cuadrados}")

# Ejemplo B: Convertir a mayúsculas para limpiar datos
def a_mayusculas(texto):
    return texto.upper()

nombres = ["Ramírez", "Nadia", "python"]
resultado_nombres = aplicar_a_lista(a_mayusculas, nombres)
print(f"Nombres corregidos: {resultado_nombres}")
