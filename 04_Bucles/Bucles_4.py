while True:
    try:
        n = int(input("Introduce un número entero positivo para la cuenta atrás: "))

        if n <= 0:
            print("Error: El número debe ser mayor que 0.")
        else:
            print(f"\nIniciando cuenta atrás desde {n}:")
            
            for i in range(n, -1, -1):
                if i > 0:
                    print(i, end=", ")
                else:
                    print(i)
            
            break

    except ValueError:
        print("Error: Has introducido un dato no válido (letras o decimales).")