def decimal_a_binario(n):
    """Convierte un número decimal entero en una cadena binaria."""
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

def binario_a_decimal(binario):
    """Convierte una cadena de texto binaria en un número decimal."""
    decimal = 0
    # Invertimos la cadena para que el índice coincida con la potencia de 2
    binario_invertido = str(binario)[::-1]
    
    for i, digito in enumerate(binario_invertido):
        if digito == '1':
            decimal += 2 ** i
            
    return decimal

# Ejemplos de uso:
num_decimal = 25
num_binario = "11001"

print(f"Decimal {num_decimal} a binario: {decimal_a_binario(num_decimal)}")
print(f"Binario {num_binario} a decimal: {binario_a_decimal(num_binario)}")