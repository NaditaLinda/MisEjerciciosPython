from abc import ABC, abstractmethod
import json
import os

# 1. CLASES BASE (Abstractas)
class Personaje(ABC):
    def __init__(self, id_personaje, nombre, nivel, vida):
        self._id = id_personaje
        self._nombre = nombre
        self._nivel = nivel
        self._vida = vida

    @abstractmethod
    def atacar(self): pass

    def recibir_danio(self, cantidad):
        self._vida -= cantidad
        print(f"{self._nombre} recibe {cantidad} de daño. Vida: {self._vida}")

    def esta_vivo(self): return self._vida > 0

    def __str__(self):
        return f"{self._nombre} (Niv: {self._nivel} | Vida: {self._vida})"

class Item(ABC):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
    @abstractmethod
    def usar(self, personaje): pass

# 2. CLASES HIJAS (Herencia y Polimorfismo)
class Jugador(Personaje):
    def __init__(self, id_p, nom, niv, vid):
        super().__init__(id_p, nom, niv, vid)
        self.experiencia = 0
        self.inventario = Inventario()

    def atacar(self):
        return 10 + self._nivel

    def ganar_exp(self, exp):
        self.experiencia += exp
        print(f"¡{self._nombre} ganó {exp} XP!")

class Enemigo(Personaje):
    def __init__(self, id_p, nom, niv, vid, tipo):
        super().__init__(id_p, nom, niv, vid)
        self.tipo = tipo

    def atacar(self):
        return 5 + self._nivel

class Pocion(Item):
    def usar(self, personaje):
        personaje._vida += 20
        print(f"Poción usada en {personaje._nombre}. +20 Vida.")

# 3. CLASES DE APOYO (Inventario, Misión, Mapa)
class Inventario:
    def __init__(self): self.items = []
    def agregar_item(self, item): self.items.append(item)

class Mision:
    def __init__(self, descripcion, recompensa_xp):
        self.descripcion = descripcion
        self.recompensa_xp = recompensa_xp
        self.completada = False

    def completar(self, jugador):
        if not self.completada:
            self.completada = True
            jugador.ganar_exp(self.recompensa_xp)
            print(f"Misión '{self.descripcion}' completada.")

class Mapa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_enemigos = []

# 4. CLASE CONTROLADORA (El cerebro del sistema)
class Juego:
    def __init__(self):
        self.jugadores = []
        self.mapas = []

    def registrar_jugador(self, nuevo_jugador: Jugador):
        """Verifica si el nombre ya existe antes de añadirlo."""
        nombres = [j._nombre.lower() for j in self.jugadores]
        if nuevo_jugador._nombre.lower() in nombres:
            print(f"❌ Error: El nombre '{nuevo_jugador._nombre}' ya existe.")
            return False
        
        self.jugadores.append(nuevo_jugador)
        return True

    def guardar_jugadores(self, nombre_archivo="jugadores.json"):
        """Convierte objetos Jugador a JSON y los guarda en disco."""
        datos_a_guardar = []
        for j in self.jugadores:
            datos_a_guardar.append({
                "id": j._id,
                "nombre": j._nombre,
                "nivel": j._nivel,
                "vida": j._vida,
                "experiencia": j.experiencia
            })

        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos_a_guardar, archivo, indent=4)
            print(f"💾 Datos guardados correctamente en {nombre_archivo}")
        except Exception as e:
            print(f"⚠️ Error al guardar: {e}")

    def cargar_jugadores(self, nombre_archivo="jugadores.json"):
        """Lee el archivo JSON y reconstruye los objetos Jugador (Instanciación)."""
        if not os.path.exists(nombre_archivo):
            print("ℹ️ No se encontró archivo de guardado previo.")
            return

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
            
            # Limpiamos la lista actual para cargar la del archivo
            self.jugadores = []
            
            for d in datos_cargados:
                # Reconstruimos el objeto (Instanciación)
                nuevo = Jugador(d["id"], d["nombre"], d["nivel"], d["vida"])
                nuevo.experiencia = d["experiencia"]
                self.jugadores.append(nuevo)
                
            print(f"📂 Se han cargado {len(self.jugadores)} jugadores desde el archivo.")
        except Exception as e:
            print(f"⚠️ Error al cargar los datos: {e}")

    def iniciar_juego(self):
        print("--- BIENVENIDO A REINOS DE PROGRAMARIA ---")

# 5. PROGRAMA PRINCIPAL (Simulación)
if __name__ == "__main__":
    mi_rpg = Juego()
    
    # 1. Intentamos cargar datos previos
    mi_rpg.cargar_jugadores()
    
    # 2. Si no hay jugadores, creamos uno nuevo
    if not mi_rpg.jugadores:
        p_nuevo = Jugador(1, "MoureDev", 1, 100.0)
        mi_rpg.registrar_jugador(p_nuevo)
        # Guardamos para la próxima vez
        mi_rpg.guardar_jugadores()
    
    # 3. Mostrar el estado actual
    for p in mi_rpg.jugadores:
        print(p)