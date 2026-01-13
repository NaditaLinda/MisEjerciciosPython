# Recibir datos y convertir a número decimal (float)
dividendo = float(input("Introduce el primer número (dividendo): "))
divisor = float(input("Introduce el segundo número (divisor): "))

# Arquitectura de control de errores
if divisor == 0:
    print("Error: No se puede dividir por cero.")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado:.2f}")