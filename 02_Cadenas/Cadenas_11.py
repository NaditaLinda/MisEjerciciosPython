# Entrada de datos
producto = input("Nombre del producto: ")
precio_texto = input("Precio unitario: ")
unidades_texto = input("Número de unidades: ")

# Limpieza y conversión
precio = float(precio_texto.replace(",", "."))
unidades = int(unidades_texto)
coste_total = precio * unidades

# Salida sin ceros a la izquierda
# Usamos solo .2f para los decimales sin forzar un ancho con ceros
print(f"\n{producto}:")
print(f"Precio:  {precio:.2f}€")
print(f"Unidades: {unidades}")
print(f"Total:   {coste_total:.2f}€")