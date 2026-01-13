telefono = input("Introduce un número (+34-XXXXXXXXX-XX): ")

partes = telefono.split("-")

numero_principal = partes[1]

print(f"El número de teléfono es: {numero_principal}")