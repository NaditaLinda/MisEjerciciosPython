# Definimos la contraseña
contrasena_guardada = "Python2025"

# Solicitamos la entrada al usuario
intento_usuario = input("Introduce la contraseña: ")

# Validación (Normalización de datos)
# Convertimos ambas a minúsculas para que la comparación sea insensible a mayúsculas
if intento_usuario.lower() == contrasena_guardada.lower():
    print("¡Acceso concedido! La contraseña coincide.")
else:
    print("Acceso denegado. La contraseña es incorrecta.")