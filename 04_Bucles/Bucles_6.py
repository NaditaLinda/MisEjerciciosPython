while True:
    try:
        altura = int(input("Introduce la altura del triángulo (entero positivo): "))

        if altura <= 0:
            print("Error: La altura debe ser mayor que cero.")
        else:
            print(f"\nTriángulo de altura {altura}:")
            
            for i in range(1, altura + 1):
                print("*" * i)
            
            break

    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")