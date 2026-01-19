while True:
    try:
        n = int(input("Introduce la altura del triángulo (entero positivo): "))

        if n <= 0:
            print("Error: La altura debe ser mayor que cero.")
        else:
            print(f"\nGenerando triángulo de altura {n}:")
            
            for i in range(1, n + 1):
                
                for j in range(2 * i - 1, 0, -2):
                    print(j, end=" ")
                
                print()
            
            break

    except ValueError:
        print("Error: Introduce un número entero válido.")