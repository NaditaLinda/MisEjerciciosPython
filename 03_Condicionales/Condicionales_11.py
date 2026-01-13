base = "Tomate, Mozzarella"
print("Bienvenido a la pizzería Bella Napoli")

tipo = input("¿Deseas una pizza vegetariana? (si/no): ").lower().strip()

# Definición de menús mediante Diccionarios (Clave: Número, Valor: Nombre)
if tipo == "si":
    tipo_pizza = "Vegetariana"
    menu = {"1": "Pimiento", "2": "Tofu"}
else:
    tipo_pizza = "No vegetariana"
    menu = {"1": "Peperoni", "2": "Jamón", "3": "Salmón"}

# Mostrar el menú dinámico
print(f"\nIngredientes {tipo_pizza}s disponibles:")
for numero, nombre in menu.items():
    print(f"{numero}. {nombre}")

# Lógica de selección flexible (Número o Nombre)
eleccion_usuario = input("\nElige tu ingrediente: ").strip()

# Busco el ingrediente
# Caso A: El usuario escribió el número (está en las claves del diccionario)
if eleccion_usuario in menu:
    ingrediente_elegido = menu[eleccion_usuario]
# Caso B: El usuario escribió el nombre (está en los valores del diccionario)
elif eleccion_usuario.capitalize() in menu.values():
    ingrediente_elegido = eleccion_usuario.capitalize()
else:
    ingrediente_elegido = "Ingrediente no reconocido"


print("-" * 30)
print(f"Has elegido una pizza {tipo_pizza}.")
print(f"Ingredientes: {base}, {ingrediente_elegido}.")