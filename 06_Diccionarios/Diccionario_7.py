cesta = {}
continuar = True

while continuar:
    articulo = input("Introduce el nombre del artículo: ")
    precio = float(input(f"Introduce el precio de '{articulo}': ").replace(",", ".").strip())
    
    cesta[articulo] = precio
    
    respuesta = input("¿Quieres añadir otro artículo? (si/no): ").lower()
    if respuesta != "si":
        continuar = False

print("\nLista de la compra")
coste_total = 0

for articulo, precio in cesta.items():
    print(f"{articulo}\t{precio}")
    coste_total += precio

print(f"Total\t{coste_total}")