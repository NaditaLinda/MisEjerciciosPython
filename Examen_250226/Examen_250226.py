import json
import os
from abc import ABC, abstractmethod
import random

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

# La Interface Equipable define el contrato para cualquier objeto que pueda ser equipado
# por un personaje
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

# Clase base para todos los estados
class Estado(ABC):
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    @abstractmethod
    def aplicar_efecto(self, personaje):
        """Define qué le pasa al personaje cada turno."""
        pass

    def reducir_turno(self):
        """Resta un turno de duración."""
        self.duracion -= 1
        return self.duracion <= 0  # Devuelve True si el estado debe eliminarse

# --- Subclases Concretas ---
class Envenenado(Estado):
    def __init__(self, duracion=3, daño_veneno=10):
        super().__init__("Envenenado", duracion)
        self.daño_veneno = daño_veneno

    def aplicar_efecto(self, personaje):
        print(f"🤢 {personaje._nombre} sufre {self.daño_veneno} de daño por veneno.")
        personaje.recibir_danio(self.daño_veneno)

class Paralizado(Estado):
    def __init__(self, duracion=2):
        super().__init__("Paralizado", duracion)

    def aplicar_efecto(self, personaje):
        print(f"⚡ {personaje._nombre} está paralizado y no puede moverse bien.")
        personaje._ataque_base -= 5  

class Somnoliento(Estado):
    def __init__(self, duracion=1):
        super().__init__("Somnoliento", duracion)

    def aplicar_efecto(self, personaje):
        print(f"😴 {personaje._nombre} tiene mucho sueño...")

class EstadoAumentoAtaque(Estado):
    def __init__(self, nombre, duracion, bono_ataque):
        super().__init__(nombre, duracion)
        self.bono_ataque = bono_ataque
        self._aplicado = False # Para saber si ya sumamos el bono

    def aplicar_efecto(self, personaje):
        if not self._aplicado:
            personaje._ataque_base += self.bono_ataque
            self._aplicado = True
            print(f"🔥 {personaje._nombre} aumenta su ataque en {self.bono_ataque} por {self.nombre}.")
        else:
            print(f"💪 {personaje._nombre} mantiene el aumento de {self.nombre}.")

    def finalizar_efecto(self, personaje):
        """Este método lo llamaremos desde aplicar_estados en Personaje"""
        personaje._ataque_base -= self.bono_ataque
        print(f"📉 El efecto de {self.nombre} ha terminado. El ataque de {personaje._nombre} vuelve a la normalidad.")

# --- 2. CLASES BASE DE PERSONAJE ---

class Personaje(ABC):
    def __init__(self, id_p, nombre, nivel, vida_max, mana_max, ataque_inicial):
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
        self._habilidades = []

    def aplicar_estados(self):
        """Actualiza y aplica los efectos de todos los estados activos."""
        for estado in self.estados[:]:
            # 1. Aplicamos el efecto (daño de veneno o aviso de buff)
            estado.aplicar_efecto(self)
            
            # 2. Reducimos el turno
            se_acabo = estado.reducir_turno()
            
            if se_acabo:
                # --- AQUÍ ESTÁ EL CAMBIO CLAVE ---
                # Si el estado tiene un método para limpiar estadísticas, lo llamamos
                if hasattr(estado, 'finalizar_efecto'):
                    estado.finalizar_efecto(self)
                
                print(f"✨ El estado {estado.nombre} de {self._nombre} ha desaparecido.")
                self.estados.remove(estado)

    def añadir_estado(self, nuevo_estado):
        """Añade un nuevo estado a la lista del personaje."""
        self.estados.append(nuevo_estado)
        print(f"⚠️ {self._nombre} ahora está {nuevo_estado.nombre}!")

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
    
    # Para que el personaje pueda aprender habilidades
    def aprender_habilidad(self, nueva_habilidad):
        self._habilidades.append(nueva_habilidad)
        print(f"📖 {self._nombre} ha aprendido: {nueva_habilidad.nombre}")

    # Método para usar una habilidad
    def ejecutar_habilidad(self, indice, objetivo):
        if 0 <= indice < len(self._habilidades):
            habilidad = self._habilidades[indice]
            
            # Validación de seguridad: ¿Tiene maná suficiente?
            if self._mana_actual >= habilidad.costo_mana:
                # La habilidad se ejecuta y ella misma debería restar el maná en su método .usar()
                habilidad.usar(self, objetivo)
            else:
                print(f"❌ {self._nombre} intentó usar {habilidad.nombre} pero no tiene maná suficiente ({self._mana_actual}/{habilidad.costo_mana})")
        else:
            print("❌ Habilidad no encontrada.")

    def narrar(self, mensaje):
        """Añade un toque narrativo a las acciones del personaje."""
        prefix = f"[{self._nombre}]:"
        print(f"💬 {prefix} {mensaje}")   

    @abstractmethod

    def ejecutar_danio_fisico(self, objetivo):
        """Este método lo implementarán las subclases (Guerrero, Mago, etc.)"""
        pass

    def atacar(self, objetivo):
        # 1. Verificación de Estados que impiden atacar
        for estado in self.estados:
            if estado.nombre == "Paralizado":
                print(f"⚡ {self._nombre} está paralizado y no puede moverse!")
                return 
            
            if estado.nombre == "Somnoliento":
                print(f"😴 {self._nombre} está demasiado cansado para atacar con fuerza...")
                return

        # 2. Tras comprobación, procede al ataque
        self.ejecutar_danio_fisico(objetivo)

    def __str__(self):
        return f"{self._nombre} ({self.__class__.__name__}) - Niv: {self._nivel} | HP: {self._vida_actual}/{self._vida_max}"
    
# --- 3. TIPOS DE PERSONAJE (Herencia y Polimorfismo) ---

class Guerrero(Personaje):
    def __init__(self, id_p, nom, niv, vid_max, mana_max, ataque):
        super().__init__(id_p, nom, niv, vid_max, mana_max, ataque)

    def ejecutar_danio_fisico(self, objetivo):
        danio = self._ataque_base
        print(f"⚔️ {self._nombre} lanza un tajo potente a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)

class Mago(Personaje):
    def __init__(self, id_p, nom, niv, vid_max, mana_max=150, ataque=20): 
        super().__init__(id_p, nom, niv, vid_max, mana_max, ataque)

    def ejecutar_danio_fisico(self, objetivo):
        # El mago suele tener poco ataque físico, 
        # pero usamos su _ataque_base (potenciado por equipo si lo tiene)
        danio = self._ataque_base
        print(f"🧙 {self._nombre} golpea débilmente con su bastón a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)

class NPC(Personaje):
    def __init__(self, id_p, nombre, dialogo):
        # Añadimos un '0' al final porque un NPC no tiene ataque base
        super().__init__(id_p, nombre, 1, 100, 0, 0) 
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
                p = clase_ref(d["id"], d["nombre"], d["nivel"], 100, 50, d.get("ataque", 15)) # Vida y maná máximos por defecto
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
            # 1. PROCESAR ESTADOS (Venenos, parálisis, etc.)
            print(f"\n--- Turno de {self.j1._nombre} ---")
            self.j1.aplicar_estados()
            self.e1.aplicar_estados()
            
            # 2. VERIFICACIÓN TRAS ESTADOS
            if not self.j1.esta_vivo() or not self.e1.esta_vivo():
                break

            # 3. ACCIÓN JUGADOR 1 (Ahora con IA aleatoria)
            if self.j1.esta_vivo():
                self.ejecutar_turno_logico(self.j1, self.e1)
            
            # 4. VERIFICACIÓN TRAS ATAQUE J1
            if not self.e1.esta_vivo():
                break
            
            # 5. ACCIÓN ENEMIGO 1 (Ahora con IA aleatoria)
            if self.e1.esta_vivo():
                self.ejecutar_turno_logico(self.e1, self.j1)
            
            # 6. MOSTRAR RESUMEN DEL TURNO
            print(f"   > {self.j1}")
            print(f"   > {self.e1}\n")

        # 7. RESULTADO FINAL
        if self.j1.esta_vivo():
            print(f"🏆 ¡{self.j1._nombre} ha ganado!")
        else:
            print(f"💀 {self.j1._nombre} ha sido derrotado...")

    def ejecutar_turno_logico(self, atacante, defensor):
        """Decide aleatoriamente entre ataque físico o habilidad."""
        # Definimos probabilidad: 40% de usar habilidad si tiene maná
        probabilidad_habilidad = 0.4
        
        if atacante._habilidades and random.random() < probabilidad_habilidad:
            # Elegimos una habilidad al azar de su lista
            habilidad = random.choice(atacante._habilidades)
            
            # Verificamos si tiene maná suficiente
            if atacante._mana_actual >= habilidad.costo_mana:
                # Usamos el método ejecutar_habilidad (que ya pusimos en Personaje)
                indice = atacante._habilidades.index(habilidad)
                atacante.ejecutar_habilidad(indice, defensor)
                return # Finaliza el turno si usa habilidad con éxito

        # Si no tiene habilidades, no tiene maná o falló la probabilidad: Ataque físico
        atacante.atacar(defensor)

# Esta es una implementación concreta que SÍ se puede instanciar
class EstadoAumentoAtaque(Estado):
    def __init__(self, nombre, duracion, bono_ataque):
        super().__init__(nombre, duracion)
        self.bono_ataque = bono_ataque

    def aplicar_efecto(self, personaje):
        # Aquí definimos qué hace el estado realmente
        print(f"💪 {personaje._nombre} se siente más fuerte por {self.nombre} (+{self.bono_ataque} ATK)")
        # Solo lo sumamos una vez o gestionamos la lógica según tu juego

# --- INSTANCIAS DE JUEGO (Pon esto antes del bloque principal) ---

# Habilidades
bola_fuego = HabilidadOfensiva("Bola de Fuego", 15, 30)
luz_sanadora = HabilidadCurativa("Luz Sanadora", 10, 25)
estado_grito = EstadoAumentoAtaque("Fuerza", 3, 5)
escudo_espinas = HabilidadBuff("Grito de Guerra", 5, estado_grito)

# Equipo
espada_hierro = Arma("Espada de Hierro", 10)
túnica_mago = Armadura("Túnica Arcana", 5)

# Estructura del Mundo
MUNDO = {
    "Nivel 1": ["Valle de los Susurros", "Cueva de los Lamentos", "Acantilado de los Gritos", "Bosque de Sombras", "Río de Olvido", "Pradera del Eco", "Gruta de Cristal", "Paso del Viento", "Llanura de Ceniza", "Torre del Vigía"],
    "Nivel 2": ["Pantano de la Desesperación", "Ruinas de Otrora", "Mina de los Enanos", "Pico Helado", "Fortaleza del Caos", "Santuario Abandonado", "Desierto de Huesos", "Oasis del Espejismo", "Cañón del Trueno", "Portal del Abismo"],
    "Nivel 3": ["Ciudadela de los Dragones", "Templo del Sol Eterno", "Bosque Encantado", "Caverna de los Ecos", "Isla de las Sombras", "Valle de la Luna", "Montaña del Destino", "Lago de los Suspiros", "Ruinas del Olvido", "Torre del Mago Supremo"],
    "Nivel 4": ["Infierno de Fuego", "Cielo de los Ángeles", "Abismo de la Locura", "Reino de los Muertos", "Dimensión del Caos", "Mundo Espejo", "Planeta de las Bestias", "Realidad Alterna", "Universo Paralelo", "Nexus del Tiempo"],
    "Nivel 5": ["Trono del Dragón", "Corona del Rey Demonio", "Sombra del Titán", "Corazón del Mundo", "Ojo del Apocalipsis", "Altar de los Dioses", "Cráter del Fin del Mundo", "Santuario de la Eternidad", "Caverna de los Secretos", "Torre de la Creación"],
    "Nivel 6": ["Dimensión del Vacío", "Reino de la Oscuridad Eterna", "Infierno de Hielo", "Cielo de las Almas Perdidas", "Abismo de la Desesperación", "Mundo Espectral", "Planeta de las Pesadillas", "Realidad Fragmentada", "Universo Alternativo", "Nexus del Infinito"],
    "Nivel 7": ["Trono del Dragón Ancestral", "Corona del Rey Demonio Supremo", "Sombra del Titán Primordial", "Corazón del Mundo Eterno", "Ojo del Apocalipsis Final", "Altar de los Dioses Antiguos", "Cráter del Fin de los Tiempos", "Santuario de la Eternidad Absoluta", "Caverna de los Secretos Prohibidos", "Torre de la Creación Divina"],
    "Nivel 8": ["Dimensión del Vacío Absoluto", "Reino de la Oscuridad Eterna Suprema", "Infierno de Hielo Infinito", "Cielo de las Almas Perdidas Eternas", "Abismo de la Desesperación Final", "Mundo Espectral Inmortal", "Planeta de las Pesadillas Eternas", "Realidad Fragmentada Absoluta", "Universo Alternativo Infinito", "Nexus del Infinito Supremo"],
    "Nivel 9": ["Trono del Dragón Ancestral Supremo", "Corona del Rey Demonio Final", "Sombra del Titán Primordial Absoluto", "Corazón del Mundo Eterno Infinito", "Ojo del Apocalipsis Final Absoluto", "Altar de los Dioses Antiguos Eternos", "Cráter del Fin de los Tiempos Final", "Santuario de la Eternidad Absoluta Infinita", "Caverna de los Secretos Prohibidos Eternos", "Torre de la Creación Divina Suprema"],
    "Nivel 10": ["Dimensión del Vacío Absoluto Final", "Reino de la Oscuridad Eterna Suprema Infinita", "Infierno de Hielo Infinito Absoluto", "Cielo de las Almas Perdidas Eternas Finales", "Abismo de la Desesperación Final Absoluto", "Mundo Espectral Inmortal Supremo", "Planeta de las Pesadillas Eternas Finales", "Realidad Fragmentada Absoluta Infinita", "Universo Alternativo Infinito Absoluto", "Nexus del Infinito Supremo Final"] 
}

if __name__ == "__main__":
    mi_rpg = Juego()
    mi_rpg.cargar_partida()
    
    # 1. SELECCIÓN DE PERSONAJE
    print("--- BIENVENIDO AL MUNDO DE ALMA-IA ---")
    if not mi_rpg.jugadores:
        print("Elige tu clase:")
        print("1. Guerrero (Brais) - Alta vida y daño físico")
        print("2. Mago (Maira) - Menos vida, pero gran poder mágico")
        opcion = input("Selecciona (1 o 2): ")
        
        if opcion == "1":
            jugador = Guerrero(1, "Brais", 1, 100, 50, 15)
        else:
            jugador = Mago(1, "Maira", 1, 80, 100, 5)
            
        mi_rpg.registrar_jugador(jugador)
        # Creamos un enemigo base para el Nivel 1.1
        enemigo = Mago(99, "Sombra del Valle", 1, 50, 30, 5)
    else:
        jugador = mi_rpg.jugadores[0]
        enemigo = Mago(99, "Espectro Errante", jugador._nivel, 60, 40, 8)

    # 2. LOCALIZACIÓN
    # Ejemplo: Nivel 1, Subnivel 1
    zona_actual = MUNDO["Nivel 1"][0]
    print(f"\n📍 Te encuentras en: {zona_actual}")
    
    # Narración inicial
    jugador.narrar("Siento una presencia oscura en esta zona...")

    # 3. EQUIPO Y HABILIDADES (Lo que ya teníamos)
    jugador.aprender_habilidad(bola_fuego)
    jugador.equipar_arma(espada_hierro)

    # 4. INICIAR COMBATE
    pelea = CombatePro(jugador, enemigo)
    pelea.iniciar()

    # 5. GUARDAR
    if input("\n¿Guardar progreso? (s/n): ").lower() == 's':
        mi_rpg.guardar_partida()