nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
direccion = input("¿Cuál es tu dirección? ")
telefono = input("¿Cuál es tu número de teléfono? ")

usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")