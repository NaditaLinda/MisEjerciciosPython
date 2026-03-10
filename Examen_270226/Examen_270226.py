import json
import os
from abc import ABC, abstractmethod
import random
from enum import Enum

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

class ResultadoCombate(Enum):
    VICTORIA = 1
    DERROTA = 2
    EMPATE = 3

class ElementoInterface(ABC):
    @abstractmethod
    def aplicar_efecto_especial(self, personaje):
        """Cada elemento tendrá un efecto único al ser usado."""
        pass

    @abstractmethod
    def calcular_ventaja(self, elemento_objetivo):
        """Retorna un multiplicador de daño según la tabla de tipos."""
        pass

class Fuego(ElementoInterface):
    def aplicar_efecto_especial(self, personaje):
        print(f"🔥 El calor aumenta el ataque de {personaje._nombre} temporalmente!")
        personaje._ataque_base += 2

    def calcular_ventaja(self, elemento_objetivo):
        if elemento_objetivo == "Planta": return 2.0
        if elemento_objetivo == "Agua": return 0.5
        return 1.0

class Agua(ElementoInterface):
    def aplicar_efecto_especial(self, personaje):
        print(f"💧 El agua refresca a {personaje._nombre} y mejora su defensa!")
        personaje._defensa += 2

    def calcular_ventaja(self, elemento_objetivo):
        if elemento_objetivo == "Fuego": return 2.0
        if elemento_objetivo == "Tierra": return 0.5
        return 1.0

class Tierra(ElementoInterface):
    def aplicar_efecto_especial(self, personaje):
        print(f"🌱 La tierra fortalece a {personaje._nombre} y aumenta su vida!")
        personaje._vida_max += 10
        personaje._vida_actual = personaje._vida_max

    def calcular_ventaja(self, elemento_objetivo):
        if elemento_objetivo == "Agua": return 2.0
        if elemento_objetivo == "Aire": return 0.5
        return 1.0

class Aire(ElementoInterface):
    def aplicar_efecto_especial(self, personaje):
        print(f"💨 El aire da velocidad a {personaje._nombre} y le permite moverse más rápido!")
        personaje._velocidad += 2

    def calcular_ventaja(self, elemento_objetivo):
        if elemento_objetivo == "Fuego": return 2.0
        if elemento_objetivo == "Tierra": return 0.5
        return 1.0
from abc import ABC, abstractmethod

class Elemento(ABC):
    @abstractmethod
    def aplicar_efecto(self, lanzador, objetivo):
        """Aplica el efecto especial del elemento (cura, defensa, etc)."""
        pass

    @abstractmethod
    def calcular_multiplicador(self, elemento_objetivo):
        """Retorna el bono de daño según la tabla de tipos."""
        pass

# --- IMPLEMENTACIÓN DE LOS ELEMENTOS ---

class Fuego(Elemento):
    def aplicar_efecto(self, lanzador, objetivo):
        print(f"🔥 ¡El calor de {lanzador._nombre} quema el ambiente!")
        # Podrías añadir un estado de 'Quemado' aquí más adelante

    def calcular_multiplicador(self, elemento_objetivo):
        if elemento_objetivo == "Aire": return 1.5  # Daño extra
        if elemento_objetivo == "Agua": return 0.5  # Debilidad
        return 1.0

class Agua(Elemento):
    def aplicar_efecto(self, lanzador, objetivo):
        if objetivo._elemento == "Tierra":
            cura = 15
            objetivo._vida_actual = min(objetivo._vida_max, objetivo._vida_actual + cura)
            print(f"💧 El agua nutre a {objetivo._nombre}. Recupera {cura} HP.")
        else:
            print(f"💧 El agua fluye alrededor de {objetivo._nombre}.")

    def calcular_multiplicador(self, elemento_objetivo):
        if elemento_objetivo == "Fuego": return 1.5
        return 1.0

class Tierra(Elemento):
    def aplicar_efecto(self, lanzador, objetivo):
        if objetivo._elemento == "Tierra":
            objetivo._defensa += 5
            print(f"⛰️ La tierra fortalece la piel de {objetivo._nombre}. Defensa +5.")

    def calcular_multiplicador(self, elemento_objetivo):
        if elemento_objetivo == "Fuego": return 0.7 # Débil frente a fuego
        return 1.0

class Aire(Elemento):
    def aplicar_efecto(self, lanzador, objetivo):
        if objetivo._elemento == "Aire":
            print(f"🌬️ Las corrientes de aire aceleran a {objetivo._nombre}.")
            # Aquí podrías aumentar una estadística de 'Velocidad' si la añades al Personaje

    def calcular_multiplicador(self, elemento_objetivo):
        if elemento_objetivo == "Tierra": return 0.6 # Muy débil frente a tierra
        return 1.0
    
# --- 2. CLASES BASE DE PERSONAJE ---

class Personaje(ABC):
    def __init__(self, id_p, nombre, nivel, vida_max, mana_max, ataque_inicial, obj_elemento):
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
        self._elemento = Elemento
        self._exp = 0
        self.instancia_elemento = obj_elemento # Guardamos la clase (Fuego, Agua, etc.)
        self._elemento = obj_elemento.__class__.__name__

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
        # 1. Calculamos el multiplicador usando la lógica de la interfaz
        multiplicador = self.instancia_elemento.calcular_multiplicador(objetivo._elemento)
        
        # 2. Aplicamos el efecto especial antes o después del daño
        self.instancia_elemento.aplicar_efecto(self, objetivo)

        # 3. Procedemos al daño físico
        self.ejecutar_danio_fisico(objetivo, multiplicador)

    def obtener_multiplicador_elemental(self, elemento_rival):
        # Tabla de tipos básica
        tabla = {
            "Fuego": {"Planta": 2.0, "Agua": 0.5},
            "Agua": {"Fuego": 2.0, "Tierra": 0.5},
            "Tierra": {"Rayo": 2.0, "Agua": 1.0},
            "Neutro": {}
        }
        return tabla.get(self._elemento, {}).get(elemento_rival, 1.0)

    @abstractmethod
    def usar_elemento(self):
        """Definido en subclases para efectos visuales o buffs."""
        pass

    def __str__(self):
        return f"{self._nombre} ({self.__class__.__name__}) - Niv: {self._nivel} | HP: {self._vida_actual}/{self._vida_max}"
    
    def restaurar_salud_y_mana(self):
        """Restaura los recursos al máximo (útil tras derrotas o descansos)."""
        self._vida_actual = self._vida_max
        self._mana_actual = self._mana_max
        self.estados = [] # Limpiamos estados alterados como veneno
        print(f"✨ {self._nombre} ha descansado. ¡Energía al máximo!")

# --- 3. TIPOS DE PERSONAJE (Herencia y Polimorfismo) ---

class Guerrero(Personaje):
    def __init__(self, id_p, nom, niv, vid_max, mana_max, ataque, obj_elemento):
        # Lo pasamos al padre (Personaje) para que él gestione la instancia
        super().__init__(id_p, nom, niv, vid_max, mana_max, ataque, obj_elemento)

    def ejecutar_danio_fisico(self, objetivo, multiplicador=1.0):
        # Ahora el daño base se ve afectado por la tabla de tipos elemental
        danio = int(self._ataque_base * multiplicador)
        print(f"⚔️ {self._nombre} lanza un tajo de {self._elemento} a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)

    def usar_elemento(self):
        print(f"🛡️ {self._nombre} imbuye su espada con el elemento {self._elemento}!")

    def cambiar_elemento(self, nuevo_elemento):
        coste_exp = 50
        if self._exp >= coste_exp:
            self._exp -= coste_exp
            print(f"🔄 {self._nombre} ha cambiado su sintonía elemental de {self._elemento} a {nuevo_elemento}!")
            self._elemento = nuevo_elemento
        else:
            print(f"❌ Necesitas {coste_exp} EXP para cambiar de elemento. (Tienes: {self._exp})")

class Mago(Personaje):
    # Asegúrate de que los argumentos coincidan con los que envías desde el 'main' o 'cargar_partida'
    def __init__(self, id_p, nom, niv, vid_max, mana_max, ataque, obj_elemento): 
        super().__init__(id_p, nom, niv, vid_max, mana_max, ataque, obj_elemento)

    def ejecutar_danio_fisico(self, objetivo, multiplicador=1.0):
        danio = int(self._ataque_base * multiplicador)
        print(f"🧙 {self._nombre} golpea con su báculo de {self._elemento} a {objetivo._nombre}!")
        objetivo.recibir_danio(danio)
        
    def usar_elemento(self):
        print(f"🔮 {self._nombre} canaliza la esencia del {self._elemento} en su báculo.")

class MisionElemental:
    def __init__(self, descripcion, elemento_requerido, recompensa_exp):
        self.descripcion = descripcion
        self.elemento_requerido = elemento_requerido
        self.recompensa_exp = recompensa_exp
        self.completada = False

    def validar_cumplimiento(self, personaje, elemento_usado_en_combate):
        if elemento_usado_en_combate == self.elemento_requerido:
            self.completada = True
            personaje._exp += self.recompensa_exp
            print(f"✅ ¡Misión Cumplida! Has ganado {self.recompensa_exp} EXP.")
            return True
        else:
            print(f"❌ No has usado el elemento {self.elemento_requerido}. Misión fallida.")
            return False
        
class NPC(Personaje):
    def __init__(self, id_p, nombre, dialogo):
        super().__init__(id_p, nombre, 1, 100, 0, 0, Fuego()) 
        
        self.dialogo = dialogo
        self.mision_activa = None
    # --- IMPLEMENTACIÓN OBLIGATORIA DE MÉTODOS ABSTRACTOS ---

    def ejecutar_danio_fisico(self, objetivo, multiplicador=1.0):
        """Los NPCs no hacen daño físico."""
        pass

    def usar_elemento(self):
        """Los NPCs no usan poderes elementales."""
        pass
    # -------------------------------------------------------

    def otorgar_mision(self, descripcion, elemento_req, exp):
        self.mision_activa = MisionElemental(descripcion, elemento_req, exp)
        print(f"📜 [{self._nombre}] te ha dado una misión: {descripcion}")

    def hablar(self):
        print(f"💬 [{self._nombre}]: {self.dialogo}")

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

    def guardar_partida(self, nivel, subnivel, archivo="savegame.json"):
        datos = {
            "progreso_mundo": {
                "nivel_actual": nivel,
                "subnivel_actual": subnivel
            },
            "personajes": []
        }
        
        for j in self.jugadores:
            datos["personajes"].append({
                "id": j._id,
                "nombre": j._nombre,
                "clase": j.__class__.__name__,
                "nivel": j._nivel,
                "elemento": j._elemento,        # <--- NUEVO: Guardamos el elemento actual
                "experiencia": j._exp,          # <--- NUEVO: Guardamos la EXP acumulada
                "vida_actual": j._vida_actual,
                "vida_max": j._vida_max, 
                "mana_actual": j._mana_actual,
                "mana_max": j._mana_max,        # <--- RECOMENDADO: Guardar también el maná máximo
                "ataque": j._ataque_base 
            })
            
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"💾 Partida guardada en el tramo {nivel}.{subnivel}")
   
    def cargar_partida(self, archivo="savegame.json"):
        if not os.path.exists(archivo):
            return 1, 1 
            
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            self.jugadores = []
            
            # --- MAPEOS DE RECONSTRUCCIÓN ---
            clase_map = {"Guerrero": Guerrero, "Mago": Mago}
            mapa_elementos = {
                "Fuego": Fuego(),
                "Agua": Agua(),
                "Tierra": Tierra(),
                "Aire": Aire(),
                "Neutro": Fuego() # Valor por defecto seguro
            }
            # -------------------------------

            progreso = datos.get("progreso_mundo", {"nivel_actual": 1, "subnivel_actual": 1})
            n_act = progreso["nivel_actual"]
            s_act = progreso["subnivel_actual"]

            for d in datos["personajes"]:
                clase_ref = clase_map.get(d["clase"], Guerrero)
                
                # Recuperamos el nombre del elemento del JSON y obtenemos el OBJETO
                nombre_elem_guardado = d.get("elemento", "Neutro")
                obj_elemento = mapa_elementos.get(nombre_elem_guardado, mapa_elementos["Neutro"])
                
                # Instanciamos al personaje con su OBJETO elemento
                p = clase_ref(
                    d["id"], 
                    d["nombre"], 
                    d["nivel"], 
                    d.get("vida_max", 100), 
                    d.get("mana_max", 50),
                    d.get("ataque", 15),
                    obj_elemento  # <--- PASAMOS EL OBJETO, NO EL TEXTO
                )
                
                p._vida_actual = d["vida_actual"]
                p._mana_actual = d["mana_actual"]
                p._exp = d.get("experiencia", 0)
                
                self.jugadores.append(p)
                
        print(f"📂 Partida cargada: {len(self.jugadores)} héroes con sus poderes elementales intactos.")
        return n_act, s_act
    
    def borrar_partida(self, archivo="savegame.json"):
        if os.path.exists(archivo):
            try:
                os.remove(archivo)
                print("🗑️ Archivo de guardado eliminado correctamente.")
                # Limpiamos también la lista de jugadores en memoria
                self.jugadores = []
                return True
            except Exception as e:
                print(f"❌ Error al borrar: {e}")
                return False
        else:
            print("❓ No se encontró ninguna partida para borrar.")
            return False

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
            return ResultadoCombate.VICTORIA
        elif not self.j1.esta_vivo() and not self.e1.esta_vivo():
            print("🤝 ¡Empate técnico! Ambos han caído.")
            return ResultadoCombate.EMPATE
        else:
            print(f"💀 {self.j1._nombre} ha sido derrotado...")
            return ResultadoCombate.DERROTA

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
    archivo_save = "savegame.json"

    # --- 1. INSERCIÓN: MAPEO DE ELEMENTOS ---
    # Coloca esto al principio para que esté disponible en todo el bloque
    MAPA_ELEMENTOS = {
        "Fuego": Fuego(),
        "Agua": Agua(),
        "Tierra": Tierra(),
        "Aire": Aire()
    }
    # ----------------------------------------

    # --- BLOQUE 1: LÓGICA DE INICIO ---
    if os.path.exists(archivo_save):
        print("\n💾 Partida detectada. 1. Continuar | 2. Nueva (Borrar)")
        if input("Selecciona: ") == "2":
            if input("⚠️ ¿Borrar? (s/n): ").lower() == 's':
                mi_rpg.borrar_partida(archivo_save)
                nivel_actual, subnivel_actual = 1, 1
            else:
                nivel_actual, subnivel_actual = mi_rpg.cargar_partida(archivo_save)
        else:
            nivel_actual, subnivel_actual = mi_rpg.cargar_partida(archivo_save)
    else:
        nivel_actual, subnivel_actual = 1, 1

    # --- BLOQUE 2: GESTIÓN DE JUGADORES ---
    if mi_rpg.jugadores:
        jugador = mi_rpg.jugadores[0]
    else:
        # --- 2. INSERCIÓN: CAMBIO AL CREAR JUGADOR ---
        # Pasamos la instancia MAPA_ELEMENTOS["Fuego"] en lugar de solo el texto "Fuego"
        jugador = Guerrero(1, "Brais", 1, 100, 50, 15, MAPA_ELEMENTOS["Fuego"])
        jugador.aprender_habilidad(bola_fuego)
        mi_rpg.jugadores.append(jugador)

    anciano = NPC(50, "Maestro Zen", "El fuego consume, pero el agua fluye...")
    anciano.otorgar_mision("Derrota al Guardián usando AGUA", "Agua", 100)

    # --- BUCLE PRINCIPAL ---
    while nivel_actual <= 10:
        while subnivel_actual <= 10:
            nombre_zona = MUNDO[f"Nivel {nivel_actual}"][subnivel_actual-1]
            intentos = 0
            max_intentos = 3
            victoria_lograda = False

            while intentos < max_intentos and not victoria_lograda:
                print(f"\n📍 {nombre_zona} ({nivel_actual}.{subnivel_actual}) - Intento {intentos+1}/{max_intentos}")
                
                # --- 3. INSERCIÓN: GENERAR ENEMIGO CON OBJETO ELEMENTO ---
                vida_e = 50 + (nivel_actual * 20) + (subnivel_actual * 8)
                ataque_e = 8 + (nivel_actual * 3) + subnivel_actual
                
                # Elegimos una clave al azar y sacamos el OBJETO del diccionario
                nombre_elem_e = random.choice(["Fuego", "Agua", "Tierra", "Aire"])
                obj_elem_e = MAPA_ELEMENTOS[nombre_elem_e]
                
                clase_enemigo = random.choice([Guerrero, Mago])
                # Pasamos obj_elem_e como último argumento
                enemigo = clase_enemigo(99, f"Guardián", nivel_actual, vida_e, 40, ataque_e, obj_elem_e)
                # ---------------------------------------------------------
                
                pelea = CombatePro(jugador, enemigo)
                resultado = pelea.iniciar() 

                if resultado == ResultadoCombate.VICTORIA:
                    print("✅ ¡VICTORIA!")
                    if anciano.mision_activa:
                        anciano.mision_activa.validar_cumplimiento(jugador, jugador._elemento)
                    
                    victoria_lograda = True
                    subnivel_actual += 1 
                    jugador._vida_actual = min(jugador._vida_max, jugador._vida_actual + 20)
                    
                elif resultado == ResultadoCombate.EMPATE:
                    if input("🤝 Empate. ¿1. Reintentar | 2. Rendirse?: ") == "2":
                        intentos = max_intentos
                    else:
                        intentos += 1
                else:
                    intentos += 1
                    print(f"❌ Caíste. Quedan {max_intentos - intentos} intentos.")
                    jugador.restaurar_salud_y_mana()

            if not victoria_lograda:
                print("💀 Game Over en este tramo.")
                nivel_actual = 11; break 
            
            if input("\n¿Quieres (G)uardar y salir o (C)ontinuar?: ").lower() == 'g':
                mi_rpg.guardar_partida(nivel_actual, subnivel_actual)
                nivel_actual = 11; subnivel_actual = 11; break

        nivel_actual += 1
        subnivel_actual = 1