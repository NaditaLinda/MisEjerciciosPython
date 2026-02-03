# --- CLASES DE GESTIÓN DE EVENTOS ---

class Atracciones:
    def __init__(self, capacidad:int, nombre, dimensiones:float, precio_entrada:float, normativa):
        self.capacidad = capacidad
        self.nombre = nombre
        self.dimensiones = dimensiones
        self.precio_entrada = precio_entrada
        self.normativa = normativa

    def mostrar_atracciones(self):
        print(f"[ATRACCIÓN] {self.nombre} - Capacidad: {self.capacidad} - Dimensiones: {self.dimensiones} - Precio: {self.precio_entrada}€ - Normativa: {self.normativa}")

class Pasarruas:
    def __init__(self, num_persoas:int, ruas, nome_pasarrua):
        self.num_persoas = num_persoas
        self.ruas = ruas
        self.nome_pasarrua = nome_pasarrua

    def mostrar_pasarruas(self):
        print(f"[PASARRÚAS] {self.nome_pasarrua} - Nº Personas: {self.num_persoas} - Recorrido: {self.ruas}")

class Concertos:
    def __init__(self, grupo, data, hora, prezo:float, lugar):
        self.grupo = grupo
        self.data = data
        self.hora = hora
        self.prezo = prezo
        self.lugar = lugar

    def mostrar_concertos(self):
        print(f"[CONCIERTO] {self.grupo} - Fecha: {self.data} a las {self.hora} - Lugar: {self.lugar} - Precio: {self.prezo}€")

# --- CLASES DE GESTIÓN CONTABLE ---

class Gastos:
    def __init__(self, codigo, denominacion, empresa, cif, cantidad:int):
        self.codigo = codigo
        self.denominacion = denominacion
        self.empresa = empresa
        self.cif = cif
        self.cantidad = cantidad

    def mostrar_gastos(self):
        print(f"[GASTO {self.codigo}] {self.denominacion} - Empresa: {self.empresa} ({self.cif}) - Total: {self.cantidad}€")

class Ingresos:
    def __init__(self, codigo, denominacion, empresa, cif, cantidad):
        self.codigo = codigo
        self.denominacion = denominacion
        self.empresa = empresa
        self.cif = cif
        self.cantidad = cantidad

    def mostrar_ingresos(self):
        print(f"[INGRESO {self.codigo}] {self.denominacion} - Cliente: {self.empresa} ({self.cif}) - Total: {self.cantidad}€")


# --- CREACIÓN DE OBJETOS (2 de cada clase) ---

# Atracciones
noria = Atracciones(50, "La Noria Gigante", "20.50 m2", 5, "Prohibido menores de 5 años")
tiovivo = Atracciones(20, "Tiovivo Clásico", "10m x 10m", 3, "Uso obligatorio de cinturón")

# Pasarrúas
charanga = Pasarruas(12, "Calle Mayor, Plaza Real", "Os Alegres")
batucada = Pasarruas(25, "Paseo Marítimo", "Ritmo Galego")

# Concertos
orquesta = Concertos("Panorama", "15/08/2026", "22:00", 0, "Plaza del Pueblo")
rock_band = Concertos("Los Linces", "16/08/2026", "23:30", 10, "Estadio Municipal")

# Gastos
luz = Gastos("G001", "Suministro Eléctrico", "IberLuz", "B12345678", 1200.50)
seguridad = Gastos("G002", "Seguridad Privada", "Securitas", "A98765432", 3500.00)

# Ingresos
entradas = Ingresos("I001", "Venta de Entradas", "Ticketea", "B55544433", 15400.00)
patrocinio = Ingresos("I002", "Patrocinio Concello", "Concello de Pontevedra", "P3600000A", 5000.00)

# --- EJECUCIÓN ---
print("--- RESUMEN DE LA PEREGRINA ---")
noria.mostrar_atracciones()
charanga.mostrar_pasarruas()
orquesta.mostrar_concertos()
luz.mostrar_gastos()
entradas.mostrar_ingresos()