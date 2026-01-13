def aplicar_descuento (precio, porcentaje):
    return precio - ((precio * porcentaje)/100)

def aplicar_iva (precio, iva_a):
    return precio + ((precio * iva_a)/100)

def procesar_cesta(cesta, funcion_a_aplicar):
    total = 0
    # Recorremos el diccionario: producto es la clave, datos (precio, %) es el valor
    for producto, datos in cesta.items():
        precio_base = datos[0]
        porcentaje = datos[1]
        
        # Aplicamos la función que hayamos pasado por parámetro
        precio_final_producto = funcion_a_aplicar(precio_base, porcentaje)
        total += precio_final_producto
        
    return total

# --- Ejemplo de uso ---
mi_cesta = {
    'Portátil': (1000, 15), # 1000€ con 15% de descuento o IVA
    'Ratón': (20, 10),      # 20€ con 10% de descuento o IVA
    'Monitor': (200, 21)    # 200€ con 21% de descuento o IVA
}

# Calculamos el precio final aplicando descuentos
precio_con_descuentos = procesar_cesta(mi_cesta, aplicar_descuento)
print(f"Total con descuentos: {precio_con_descuentos}€")

# Calculamos el precio final aplicando IVA
precio_con_iva = procesar_cesta(mi_cesta, aplicar_iva)
print(f"Total con IVA: {precio_con_iva}€")