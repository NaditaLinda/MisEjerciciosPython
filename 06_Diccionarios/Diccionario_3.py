precios_frutas = {
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

fruta = input("¿Qué fruta quieres comprar? ").title()
kilos = input("¿Cuántos kilos necesitas? ")

if fruta in precios_frutas:
    # Convertimos los kilos a número decimal (float) para poder operar
    cantidad_kilos = float(kilos)
    precio_unitario = precios_frutas[fruta]
    coste_total = precio_unitario * cantidad_kilos
    
    print(f"{cantidad_kilos}kg de {fruta} cuestan {coste_total:.2f}€")
else:
    print(f"Lo sentimos, la fruta '{fruta}' no está disponible.")