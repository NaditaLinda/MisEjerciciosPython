# 1. Entrada de datos
# Usamos int() porque el enunciado pide un número entero
n = int(input("Introduce un número entero positivo: "))

# 2. Cálculo usando la fórmula de Gauss
# Usamos // para que el resultado sea un entero (división entera)
suma = (n * (n + 1)) // 2

# 3. Salida por pantalla
print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")
