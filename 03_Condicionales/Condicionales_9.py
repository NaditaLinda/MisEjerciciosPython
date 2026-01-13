entrada_edad = input("Por favor ingresa tu edad: ")

try:
    edad = int(entrada_edad)

    if edad <4:
        precio = 0
        mensaje = "Entras gratis por ser menor de 4 años"
    elif 4 <= edad <= 18:
        precio=5
        mensaje = f"El precio de tu entrada es de {precio} €."
    else:
        precio=10
        mensaje = f"El precio de tu entrada es de {precio} €."
    
    print(f"\nResultado para {edad} años:")
    print(mensaje)

except ValueError:
    print("Error: '{entrada_edad}' no es una edad válida. Introduce un número entero")
