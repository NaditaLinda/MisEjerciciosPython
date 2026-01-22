def calcular_mcd(a, b):
    """
    Calcula el Máximo Común Divisor de dos números usando el Algoritmo de Euclides.
    """
    while b:
        # Aplicamos la lógica: mcd(a, b) = mcd(b, a % b)
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    """
    Calcula el Mínimo Común Múltiplo de dos números basándose en su MCD.
    """
    if a == 0 or b == 0:
        return 0
    
    # Aplicamos la fórmula: mcm(a, b) = |a * b| / mcd(a, b)
    # Usamos // para obtener una división entera
    mcd = calcular_mcd(a, b)
    return abs(a * b) // mcd

# Ejemplo de uso:
num1 = 48
num2 = 18

print(f"El MCD de {num1} y {num2} es: {calcular_mcd(num1, num2)}")
print(f"El MCM de {num1} y {num2} es: {calcular_mcm(num1, num2)}")