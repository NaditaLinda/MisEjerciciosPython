def calcular_suma_gauss():
    n = 0

    while True:
        entrada = input("Introduce un número entero positivo: ")
        try:
            n = int(entrada)
            if n > 0:
                break
            else:
                print("Error: El número debe ser mayor que 0. Inténtalo de nuevo.")
        except ValueError:
            print(f"Error: '{entrada}' no es un número entero válido")

    # Uso la fórmula de gauss y // para que el resultado sea un entero (división entera)
    suma = (n * (n + 1)) // 2

    # Muestro por pantalla
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

if __name__ == "__main__":
    calcular_suma_gauss()


