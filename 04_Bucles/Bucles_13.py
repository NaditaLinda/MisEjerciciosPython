while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        print("Programa terminado. ¡Adiós!")
        break  # Rompe el bucle y sale
    
    print(f"Eco: {entrada}")