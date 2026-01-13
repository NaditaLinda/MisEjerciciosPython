PRECIO_HABITUAL = 2.30
DESCUENTO_PORCENTAJE = 0.60 

barras_no_frescas = int(input("Introduce el número de barras vendidas que no son del día: "))

descuento_por_barra = PRECIO_HABITUAL * DESCUENTO_PORCENTAJE
precio_con_descuento = PRECIO_HABITUAL - descuento_por_barra
coste_final_total = barras_no_frescas * precio_con_descuento

print(f"Precio habitual de una barra: {PRECIO_HABITUAL}€")
print(f"Descuento por no ser fresca: {round(descuento_por_barra, 2)}€")
print(f"Coste final total: {round(coste_final_total, 2)}€")