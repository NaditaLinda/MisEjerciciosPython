BONIFICACION_BASE = 2400

puntuacion_usuario = input("Introduce la puntuación (0.0, 0.4, 0.6 o más): ")
puntuacion_usuario = puntuacion_usuario.replace(',', '.')

try:
    puntuacion = float(puntuacion_usuario)

    nivel = ""
    error = False

    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion == 0.6:
        nivel = "Bueno"
    else:
        error = True

    if error:
        print ("Error: La puntuación intriducida no es válida (No se permiten valores intermedios)")
    else:
        cantidad_dinero = puntuacion * BONIFICACION_BASE
        print(f"\nNivel de rendimiento: **{nivel}**")
        print(f"Cantidad de dinero recibida: **{cantidad_dinero:.2f}€**")

except ValueError:
    print("Error: Por favor introduce un número válido")

