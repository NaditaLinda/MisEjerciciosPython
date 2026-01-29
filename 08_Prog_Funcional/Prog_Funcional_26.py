# Datos: Velocidad (km/h), Dirección y Presión (hPa)
registros_enero = [
    {"fecha": "2026-01-05", "viento": 85, "dir": "SW", "presion": 995},
    {"fecha": "2026-01-06", "viento": 40, "dir": "W", "presion": 1012},
    {"fecha": "2026-01-07", "viento": 95, "dir": "NW", "presion": 988},
    {"fecha": "2026-01-08", "viento": 20, "dir": "N", "presion": 1025},
    {"fecha": "2026-01-09", "viento": 75, "dir": "S", "presion": 1002}
]

# Definición del criterio de Vendaval (Lambda)
# Condición: Viento > 70 km/h Y Presión < 1000 hPa Y Dirección en sectores atlánticos
es_vendaval = lambda d: d["viento"] > 70 and \
                        d["presion"] < 1000 and \
                        d["dir"] in ["SW", "W", "NW"]

# Aplicación del filtro
episodios_criticos = list(filter(es_vendaval, registros_enero))

# Visualización
print(f"Alerta de Vendaval: {len(episodios_criticos)} episodios detectados.")
for ep in episodios_criticos:
    print(f"- {ep['fecha']}: {ep['viento']} km/h desde el {ep['dir']} ({ep['presion']} hPa)")