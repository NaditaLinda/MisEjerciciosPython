while True:
    try:
        n = int(input("Introduce un número entero: "))

        if n <= 0:
            print("El número debe ser positivo")
        else:
            print(f"\nLos números impares hasta {n} son: ")
            for i in range(1, n + 1, 2):
                if i + 2 > n:
                    print(f"{i}.")
                else:
                    print(f"{i}", end=",")
            break
    except ValueError:
        print("Error: Debes introducir un número entero válido.")