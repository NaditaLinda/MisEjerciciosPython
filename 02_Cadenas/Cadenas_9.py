fecha_usuario = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

partes = fecha_usuario.split("/")

dia = partes[0]
mes = partes[1]
anio = partes[2]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")