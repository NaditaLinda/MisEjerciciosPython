# Datos de entrada: Lista de árboles
arboles = [
    {"especie": "Carballo", "edad": 150, "estado": "buen estado"},
    {"especie": "Sobreira", "edad": 80, "estado": "buen estado"},
    {"especie": "Castiñeiro", "edad": 210, "estado": "enfermo"},
    {"especie": "Faia", "edad": 110, "estado": "buen estado"},
    {"especie": "Piñeiro", "edad": 95, "estado": "regular"}
]

# Lógica de filtrado (Lambda con condición compuesta)
# Condición: edad >= 100 Y estado == "buen estado"
criterio_seleccion = lambda a: a["edad"] >= 100 and a["estado"] == "buen estado"

# Aplicación del filtro
# filter() recorre la lista y solo mantiene los elementos que cumplen la lambda
arboles_seleccionados = list(filter(criterio_seleccion, arboles))

# Visualización de resultados
print("Árboles centenarios en buen estado:")
for arbol in arboles_seleccionados:
    print(f"- {arbol['especie']} ({arbol['edad']} años)")