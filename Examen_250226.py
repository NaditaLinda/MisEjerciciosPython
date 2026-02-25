import json
import os
from abc import ABC, abstractmethod

# --- 1. SISTEMA DE APOYO Y ESTADOS ---

class EstadoAlterado:
    def __init__(self, nombre, duracion, danio_por_turno=0):
        self.nombre = nombre
        self.duracion = duracion
        self.danio_por_turno = danio_por_turno

class Item(ABC):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
    @abstractmethod
    def usar(self, personaje): pass

class Habilidad(ABC):
    def __init__(self, nombre, costo_mana):
        self.nombre = nombre
        self.costo_mana = costo_mana

    @abstractmethod
    def usar(self, lanzador, objetivo):
        """Define qué hace la habilidad al ser usada."""
        pass

    # 1. Subclase Ofensiva (Hace daño)
class HabilidadOfensiva(Habilidad):
    def __init__(self, nombre, costo_mana, potencia_danio):
        super().__init__(nombre, costo_mana)
        self.potencia_danio = potencia_danio

    def usar(self, ejecutor, objetivo):
        print(f"🔥 {ejecutor._nombre} lanza {self.nombre}!")
        objetivo.recibir_danio(self.potencia_danio)

# 2. Subclase Curativa (Restaura HP)
class HabilidadCurativa(Habilidad):
    def __init__(self, nombre, costo_mana, potencia_cura):
        super().__init__(nombre, costo_mana)
        self.potencia_cura = potencia_cura

    def usar(self, ejecutor, objetivo):
        print(f"💚 {ejecutor._nombre} usa {self.nombre} sobre {objetivo._nombre}")
        # Sanamos al objetivo (puede ser uno mismo)
        objetivo._vida_actual = min(objetivo._vida_max, objetivo._vida_actual + self.potencia_cura)

# 3. Subclase Buff (Añade un estado beneficioso)
class HabilidadBuff(Habilidad):
    def __init__(self, nombre, costo_mana, estado):
        super().__init__(nombre, costo_mana)
        self.estado = estado # Aquí pasas un objeto de tipo Estado

    def usar(self, ejecutor, objetivo):
        print(f"🛡️ {ejecutor._nombre} aplica {self.nombre} a {objetivo._nombre}")
        objetivo.estados.append(self.estado)

class BolaDeFuego(Habilidad):
    def __init__(self):
        super().__init__("Bola de Fuego", 20)

    def usar(self, lanzador, objetivo):
        if lanzador.consumir_mana(self.costo_mana):
            danio = 30 + lanzador._nivel
            print(f"🔥 {lanzador._nombre} lanza {self.nombre}!")
            objetivo.recibir_danio(danio)

class Pocion(Item):
    def usar(self, personaje):
        personaje._vida_actual = min(personaje._vida_max, personaje._vida_actual + 20)
        print(f"🧪 {personaje._nombre} usa {self.nombre} y recupera 20 HP.")

from abc import ABC, abstractmethod

# La Interface (Contrato)
class Equipable(ABC):
    @abstractmethod
    def equipar(self, personaje):
        pass

    @abstractmethod
    def desequipar(self, personaje):
        pass

# Implementación: Arma
class Arma(Equipable):
    def __init__(self, nombre, bono_ataque):
        self.nombre = nombre
        self.bono_ataque = bono_ataque

    def equipar(self, personaje):
        # Aumentamos el ataque base del personaje
        personaje._ataque_base += self.bono_ataque
        print(f"⚔️ {self.nombre} equipada (+{self.bono_ataque} ATK)")

    def desequipar(self, personaje):
        personaje._ataque_base -= self.bono_ataque
        print(f"❌ {self.nombre} desequipada.")

# Implementación: Armadura
class Armadura(Equipable):
    def __init__(self, nombre, bono_defensa):
        self.nombre = nombre
        self.bono_defensa = bono_defensa

    def equipar(self, personaje):
        # Aumentamos la defensa del personaje
        personaje._defensa += self.bono_defensa
        print(f"🛡️ {self.nombre} equipada (+{self.bono_defensa} DEF)")

    def desequipar(self, personaje):
        personaje._defensa -= self.bono_defensa
        print(f"❌ {self.nombre} desequipada.")

# --- 2. CLASES BASE DE PERSONAJE ---

class Personaje(ABC):
    def __init__(self, id_p, nombre, nivel, vida_max, mana_max):
        self._id = id_p
        self._nombre = nombre
        self._nivel = nivel
        self._vida_max = vida_max
        self._vida_actual = vida_max
        self._mana_max = mana_max
        self._mana_actual = mana_max
        self.estados = []

        self._ataque_base = ataque_inicial
        self._defensa = 0
        self._arma_equipada = None
        self._armadura_equipada = None

    def aplicar_estados(self):
        for estado in self.estados[:]:
            if estado.danio_por_turno > 0:
                print(f"🔥 {self._nombre} sufre {estado.danio_por_turno} por {estado.nombre}")
                self.recibir_danio(estado.danio_por_turno)
            estado.duracion -= 1
            if estado.duracion <= 0:
                self.estados.remove(estado)

    def equipar_arma(self, nueva_arma):
            if self._arma_equipada:
                self._arma_equipada.desequipar(self)
            self._arma_equipada = nueva_arma
            self._arma_equipada.equipar(self)

    def equipar_armadura(self, nueva_armadura):
        if self._armadura_equipada:
            self._armadura_equipada.desequipar(self)
        self._armadura_equipada = nueva_armadura
        self._armadura_equipada.equipar(self)

    def recibir_danio(self, cantidad):
        danio_mitigado = max(0, cantidad - self._defensa)
        self._vida_actual = max(0, self._vida_actual - danio_mitigado)
        print(f"💥 {self._nombre} recibe {danio_mitigado} de daño (Defensa: {self._defensa})")

    def esta_vivo(self):
        return self._vida_actual > 0
 
    def consumir_mana(self, cantidad):
        if self._mana_actual >= cantidad:
            self._mana_actual -= cantidad
            return True
        print(f"❌ {self._nombre} no tiene suficiente maná.")
        return False
    
    def ejecutar_habilidad(self, habilidad, objetivo):
        # Usamos tu método existente consumir_mana
        if self.consumir_mana(habilidad.costo_mana):
            # Aquí ocurre el Polimorfismo: no importa qué tipo de habilidad sea, 
            # el método .usar() ejecutará la lógica correcta.
            habilidad.usar(self, objetivo)

    @abstractmethod
    def atacar(self, objetivo): pass

    def __str__(self):
        return f"{self._nombre} ({self.__class__.__name__}) - Niv: {self._nivel} | HP: {self._vida_actual}/{self._vida_max}"

# --- 3. TIPOS DE PERSONAJE (Herencia y Polimorfismo) ---

class Guerrero(Personaje):
    def __init__(self, id_p, nom, niv, vid_max, mana_max):
        # Pasamos los 5 parámetros al __init__ de Personaje
        super().__init__(id_p, nom, niv, vid_max, mana_max)

    def atacar(self, objetivo):
        danio = 15 + (self._nivel * 3)
        print(f"⚔️ {self._nombre} lanza un tajo potente a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)

class Mago(Personaje):
    def __init__(self, id_p, nom, niv, vid_max, mana_max=150): # Valor por defecto
        super().__init__(id_p, nom, niv, vid_max, mana_max)

    def atacar(self, objetivo):
        # Ataque básico que no consume maná (o consume poco)
        danio = 10 + (self._nivel * 5)
        quemadura = EstadoAlterado("Quemadura", 2, 5)
        objetivo.estados.append(quemadura)
        print(f"🔥 {self._nombre} lanza una bola de fuego a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)

class NPC(Personaje):
    def __init__(self, id_p, nombre, dialogo):
        # Un NPC suele tener vida pero no nivel de combate activo
        super().__init__(id_p, nombre, 1, 100, 0)
        self.dialogo = dialogo

    def hablar(self):
        print(f"[{self._nombre}]: {self.dialogo}")

    def atacar(self, objetivo):
        print(f"{self._nombre} no es un combatiente.")

# --- 4. GESTIÓN DE JUEGO (Cerebro del sistema) ---

class Juego:
    def __init__(self):
        self.jugadores = []

    def registrar_jugador(self, nuevo_jugador):
        nombres = [j._nombre.lower() for j in self.jugadores]
        if nuevo_jugador._nombre.lower() in nombres:
            print(f"❌ Error: El nombre '{nuevo_jugador._nombre}' ya está en uso.")
            return False
        self.jugadores.append(nuevo_jugador)
        return True

    def guardar_partida(self, archivo="savegame.json"):
        datos = []
        for j in self.jugadores:
            datos.append({
                "id": j._id,
                "nombre": j._nombre,
                "clase": j.__class__.__name__,
                "nivel": j._nivel,
                "vida": j._vida_actual,
                "mana": j._mana_actual 
            })
   
    def cargar_partida(self, archivo="savegame.json"):
        if not os.path.exists(archivo): return
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            self.jugadores = []
            clase_map = {"Guerrero": Guerrero, "Mago": Mago}
            for d in datos:
                clase_ref = clase_map.get(d["clase"], Guerrero)
                # AHORA PASAMOS 5 ARGUMENTOS: id, nombre, nivel, vida_max, mana_max
                p = clase_ref(d["id"], d["nombre"], d["nivel"], 100, 50) 
                p._vida_actual = d["vida"]
                p._mana_actual = d.get("mana", 50) # Recuperamos el maná guardado
                self.jugadores.append(p)
        print(f"📂 Se han cargado {len(self.jugadores)} jugadores.")

# --- 5. SISTEMA DE COMBATE ---

class CombatePro:
    def __init__(self, j1, e1):
        self.j1 = j1
        self.e1 = e1

    def iniciar(self):
        print(f"\n--- INICIO DEL COMBATE: {self.j1._nombre} vs {self.e1._nombre} ---")
        while self.j1.esta_vivo() and self.e1.esta_vivo():
            self.j1.aplicar_states = self.j1.aplicar_estados() # Procesar venenos/fuego
            self.e1.aplicar_estados()
            
            if self.j1.esta_vivo():
                self.j1.atacar(self.e1)
            
            if self.e1.esta_vivo():
                self.e1.atacar(self.j1)
            
            print(f"  > {self.j1}\n  > {self.e1}\n")

# --- 6. PROGRAMA PRINCIPAL ---

if __name__ == "__main__":
    mi_rpg = Juego()
    
    # Intentar cargar
    mi_rpg.cargar_partida()
    
    # Si está vacío, creamos personajes iniciales
    if not mi_rpg.jugadores:
        g = Guerrero(1, "Brais", 5, 120, 20) 
        m = Mago(2, "Maira", 5, 80, 100)
        
        mi_rpg.registrar_jugador(g)
        mi_rpg.registrar_jugador(m)
        mi_rpg.guardar_partida()

    # Simular un combate entre los dos jugadores cargados
    if len(mi_rpg.jugadores) >= 2:
        pelea = CombatePro(mi_rpg.jugadores[0], mi_rpg.jugadores[1])
        pelea.iniciar()

# --- 1. Creamos una Habilidad Ofensiva ---
# Nombre: "Bola de Fuego", Costo: 15 MP, Daño: 30
bola_fuego = HabilidadOfensiva("Bola de Fuego", 15, 30)

# --- 2. Creamos una Habilidad Curativa ---
# Nombre: "Luz Sanadora", Costo: 10 MP, Curación: 25
luz_sanadora = HabilidadCurativa("Luz Sanadora", 10, 25)

# --- 3. Creamos una Habilidad de Buff (Necesita un objeto Estado) ---
# Primero definimos un pequeño objeto Estado como los que ya usa tu clase Personaje
class Estado:
    def __init__(self, nombre, duracion, danio_por_turno):
        self.nombre = nombre
        self.duracion = duracion
        self.danio_por_turno = danio_por_turno

# Nombre: "Escudo de Espinas", Costo: 5 MP
# Este buff aplicará un estado que (por ahora) no hace daño pero dura 3 turnos
escudo_espinas = HabilidadBuff("Escudo de Espinas", 5, Estado("Protección", 3, 0))
