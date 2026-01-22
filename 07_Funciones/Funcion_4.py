def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """
    Calcula el total de una factura aplicando el IVA.
    Si no se especifica el porcentaje, se aplica el 21% por defecto.
    """
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    return total

# Ejemplos de uso:
# Usando el IVA por defecto (21%)
factura_1 = calcular_total_factura(100)
print(f"Total con 21% de IVA: {factura_1} €")

# Especificando un IVA diferente (por ejemplo, el 10%)
factura_2 = calcular_total_factura(100, 10)
print(f"Total con 10% de IVA: {factura_2} €")