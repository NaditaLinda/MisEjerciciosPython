def buscar_inmuebles(lista_inmuebles, presupuesto):
    """
    Filtra inmuebles por presupuesto y añade el precio calculado.
    """
    # Definimos el año actual para el cálculo de antigüedad
    AÑO_ACTUAL = 2026
    inmuebles_en_presupuesto = []

    for inmueble in lista_inmuebles:
        # Extraer datos para el cálculo
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = 1 if inmueble['garaje'] else 0  # True vale 1, False vale 0
        antiguedad = AÑO_ACTUAL - inmueble['año']
        zona = inmueble['zona']

        # Calcular el precio base según la fórmula
        # (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad/100)
        precio_base = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)

        # Aplicar multiplicador según zona
        if zona == 'B':
            precio_final = precio_base * 1.5
        else:
            precio_final = precio_base

        # Filtrar por presupuesto
        if precio_final <= presupuesto:
            # Creamos una copia para no modificar la lista original (buena práctica)
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio_final
            inmuebles_en_presupuesto.append(inmueble_con_precio)

    return inmuebles_en_presupuesto

# --- Datos de prueba ---
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

mi_presupuesto = 100000
resultados = buscar_inmuebles(inmuebles, mi_presupuesto)

print(f"🏠 Inmuebles encontrados para un presupuesto de {mi_presupuesto}€:")
for r in resultados:
    print(r)