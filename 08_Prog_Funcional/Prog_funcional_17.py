# Datos iniciales: Alturas de faros (Torre de Hércules, Vilán, Fisterra, Estaca de Bares)
alturas_originales = [55, 24, 17, 33]

# Parámetro de corrección (Nivel medio del mar en metros)
offset_mar = 2.15

# Aplicación de la transformación con map y lambda
# La lambda recibe 'h' (altura) y devuelve 'h + offset'
alturas_corregidas = list(map(lambda h: round(h + offset_mar, 2), alturas_originales))

# Visualización de resultados
print(f"Alturas originales: {alturas_originales}")
print(f"Alturas corregidas: {alturas_corregidas}")