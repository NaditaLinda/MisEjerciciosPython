print("Bienvenido a la pizzería Bella Napoli")
base = "Tomate, Mozzarella"

tipo = input("¿Dseas una pizza vegetariana? (si/no): ").lower(). strip()

if tipo == "si":
    tipo_pizza = "Vegetariana"
    print("\nIngredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    eleccion = input("Elige un ingrediente: ").capitalize().strip()

    ingredientes_finales = f"{base}, {eleccion}"

else:
    tipo_pizza = "No Vegetariana"
    print("\nIngredientes disponibles: ")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    eleccion = input("Elige un ingrediente: ").capitalize().strip()

    ingredientes_finales = f"{base}, {eleccion}"

print("-" * 30)
print(f"Has elegido una pizza {tipo_pizza}.")
print(f"Los ingredientes que lleva son: {ingredientes_finales}.")
