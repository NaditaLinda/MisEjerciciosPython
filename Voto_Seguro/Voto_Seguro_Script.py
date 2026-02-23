import random

# --- REUTILIZAMOS NUESTRAS CLASES (RESUMIDAS) ---

class Votante:
    def __init__(self, dni, nombre, mesa_id):
        self.dni = dni
        self.nombre = nombre
        self.mesa_id = mesa_id
        self.ha_votado_en_cabina = False
        self.ha_depositado_urna = False

class Mesa:
    def __init__(self, id_mesa):
        self.id_mesa = id_mesa
        self.censo = {}
        self.votos_fisicos = 0

class ColegioElectoral:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = {}
        self.votos_candidatos = {"Partido A": 0, "Partido B": 0, "Blanco": 0, "Nulo": 0}
        self.conteo_cabina_total = 0

    def registrar_voto_cabina(self, votante, eleccion):
        self.votos_candidatos[eleccion] += 1
        self.conteo_cabina_total += 1
        votante.ha_votado_en_cabina = True

# --- FASE 1: CONFIGURACIÓN (UN MES ANTES - JEC) ---

colegio = ColegioElectoral("Colegio Público Cervantes")

# Creamos 2 mesas en este colegio
colegio.mesas["Mesa-1A"] = Mesa("Mesa-1A")
colegio.mesas["Mesa-1B"] = Mesa("Mesa-1B")

# Cargamos un censo de prueba (5 votantes)
censo_test = [
    Votante("12345678A", "Ana García", "Mesa-1A"),
    Votante("87654321B", "Juan Pérez", "Mesa-1A"),
    Votante("11223344C", "Marta López", "Mesa-1B"),
    Votante("55667788D", "Carlos Ruiz", "Mesa-1B"),
    Votante("99001122E", "Elena Sanz", "Mesa-1B")
]

# Distribuimos los votantes en sus mesas correspondientes
for v in censo_test:
    colegio.mesas[v.mesa_id].censo[v.dni] = v

print(f"--- SISTEMA INICIADO: {colegio.nombre} ---")
print(f"Mesas activas: {list(colegio.mesas.keys())}\n")

# --- FASE 2: PROCESO EN CABINA (PUNTO 1) ---

def simulacion_cabina(dni, eleccion):
    # Buscamos al votante en el colegio
    votante = None
    for m in colegio.mesas.values():
        if dni in m.censo:
            votante = m.censo[dni]
    
    if votante and not votante.ha_votado_en_cabina:
        colegio.registrar_voto_cabina(votante, eleccion)
        print(f"[CABINA] Voto impreso para DNI {dni}. Diríjase a la {votante.mesa_id}.")
    else:
        print(f"[CABINA] Error: DNI {dni} no autorizado o ya votó.")

# Simulamos 3 personas votando en cabina
simulacion_cabina("12345678A", "Partido A")
simulacion_cabina("11223344C", "Blanco")
simulacion_cabina("55667788D", "Partido B")

# --- FASE 3: IDENTIFICACIÓN EN MESA (PUNTO 2) ---

def simulacion_mesa(dni, mesa_id):
    mesa = colegio.mesas[mesa_id]
    if dni in mesa.censo:
        votante = mesa.censo[dni]
        if votante.ha_votado_en_cabina and not votante.ha_depositado_urna:
            votante.ha_depositado_urna = True
            mesa.votos_fisicos += 1
            print(f"[MESA {mesa_id}] Check realizado. Voto depositado en urna.")
        else:
            print(f"[MESA {mesa_id}] Error: El votante no ha pasado por cabina.")
    else:
        print(f"[MESA {mesa_id}] Error: Votante no pertenece a esta mesa.")

# Solo 2 de los 3 que fueron a cabina llegan a la mesa
simulacion_mesa("12345678A", "Mesa-1A")
simulacion_mesa("11223344C", "Mesa-1B")

# --- FASE 4: CIERRE Y ESCRUTINIO (PUNTOS 3, 4 y 6) ---

print("\n--- ESCRUTINIO FINAL ---")
votos_totales_mesas = 0

for id_m, m in colegio.mesas.items():
    abstenciones = len(m.censo) - m.votos_fisicos
    votos_totales_mesas += m.votos_fisicos
    print(f"Resultados {id_m}: Votos en Urna: {m.votos_fisicos} | Abstenciones: {abstenciones}")

# Verificación Punto 4
if votos_totales_mesas == colegio.conteo_cabina_total:
    print("\nVERIFICACIÓN CORRECTA: Los votos de las mesas coinciden con el colegio.")
else:
    # Esto pasará en nuestra simulación porque un votante (55667788D) votó en cabina pero NO fue a la mesa
    print(f"\nALERTA: Discrepancia detectada. Cabina: {colegio.conteo_cabina_total} / Urnas: {votos_totales_mesas}")