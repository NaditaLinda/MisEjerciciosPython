cesta = input("Introduce los productos de la cesta separados por comas: ")

lista_productos = cesta.split(",")

for producto in lista_productos:
    # Usamos .strip() para quitar espacios introducidos al escribir
    print(producto.strip())