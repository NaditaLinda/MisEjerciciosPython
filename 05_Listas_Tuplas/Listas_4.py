numeros_ganadores = []

print("Introduce los 6 números ganadores de la Primitiva (1-49):")

for i in range(6):
    # Creamos un bucle infinito que solo se rompe si el número es correcto
    while True:
        num = int(input(f"Número {i+1}: "))
        
        # Validación: ¿Está entre 1 y 49?
        if 1 <= num <= 49:
            numeros_ganadores.append(num)
            break  # Salimos del bucle 'while' y vamos al siguiente número
        else:
            print("¡Error! El número debe estar entre 1 y 49. Inténtalo de nuevo.")

# Ordenamos y mostramos
numeros_ganadores.sort()
print("\nLos números ganadores ordenados son:")
print(numeros_ganadores)