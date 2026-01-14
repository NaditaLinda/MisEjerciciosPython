try:
    edad = int(input("Cuántos años tienes?"))

    if edad <= 0:
        print("Edad no válida, debe ser un número positivo")
    else:
        print(f"\nHas cumplido estos años:")
        for i in range(1, edad + 1):
            print(f"Año {i}")
except ValueError:
    print("Por favor introduce un número válido.")
    
