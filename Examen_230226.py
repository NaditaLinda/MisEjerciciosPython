from abc import ABC, abstractmethod

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

    def registrar_jugador(self, nuevo_jugador):
        # Validación de nombre duplicado
        nombres = [j._nombre.lower() for j in self.jugadores]
        if nuevo_jugador._nombre.lower() in nombres:
            print(f"Error: El nombre {nuevo_jugador._nombre} ya existe.")
            return False
        self.jugadores.append(nuevo_jugador)
        return True

    def iniciar_juego(self):
        print("--- BIENVENIDO A REINOS DE PROGRAMARIA ---")

# 5. PROGRAMA PRINCIPAL (Simulación)
if __name__ == "__main__":
    rpg = Juego()
    
    # Intento de registro
    p1 = Jugador(1, "Brais", 1, 100)
    p2 = Jugador(2, "Brais", 1, 100) # Duplicado
    
    if rpg.registrar_jugador(p1):
        print("Jugador 1 registrado.")
    if not rpg.registrar_jugador(p2):
        print("Jugador 2 rechazado por nombre duplicado.")

    # Simular Misión
    mision_inicio = Mision("Derrotar al primer slime", 50)
    mision_inicio.completar(p1)