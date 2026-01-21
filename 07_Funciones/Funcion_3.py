def calcular_factorial(n):
    # Caso base: el factorial de 0 y 1 es siempre 1
    if n == 0 or n == 1:
        return 1
    
    # Inicialización del acumulador
    resultado = 1
    
    # Bucle multiplicador
    for i in range(2, n + 1):
        resultado *= i  # Es lo mismo que: resultado = resultado * i
        
    return resultado

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")