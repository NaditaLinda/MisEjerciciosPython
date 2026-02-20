import random

class Candidato:
    def __init__(self, nombre, partido, foto_url, logo_url):
        self.nombre = nombre
        self.partido = partido
        self.foto_url = foto_url
        self.logo_url = logo_url

class Votante:
    def __init__(self, dni, nombre, mesa_id):
        self.dni = dni
        self.nombre = nombre
        self.mesa_id = mesa_id
        self.ha_votado_en_cabina = False  # Paso 1 completado
        self.ha_depositado_urna = False    # Paso 2 completado

class MesaElectoral:
    def __init__(self, id_mesa):
        self.id_mesa = id_mesa
        self.censo_mesa = {}  # {dni: Objeto Votante}
        self.votos_fisicos = {"validos": 0, "blanco": 0, "nulo": 0}
        self.incidencias = []

    def registrar_incidencia(self, descripcion):
        self.incidencias.append(descripcion)

    def obtener_abstenciones(self):
        # Punto 6: Censo total menos los que realmente depositaron el voto
        total_censo = len(self.censo_mesa)
        votantes_reales = sum(1 for v in self.censo_mesa.values() if v.ha_depositado_urna)
        return total_censo - votantes_reales
    
    def anotar_incidencia(self, tipo, observacion):
        """
        Permite registrar si un voto impreso como válido se anula físicamente por decisión de la mesa.
        No se registra DNI, pero sí el tipo de incidencia y una observación. (Por ejemplo el voto impreso era a 
        favor de un candidato pero pasa a ser nulo por decisión de la mesa o que pase a ser blanco porque el 
        sobre esté vacío )
        """
        registro = {
            "tipo": tipo, # Ej: "Anulado físico", "Voto por correo"
            "detalle": observacion
        }
        self.incidencias.append(registro)
    
        if tipo == "Anulado físico":
            self.votos_fisicos["validos"] -= 1
            self.votos_fisicos["nulo"] += 1

class ColegioElectoral:
    def __init__(self, nombre_sitio):
        self.nombre = nombre_sitio
        self.mesas = {}  # Diccionario de objetos MesaElectoral {id_mesa: objeto}
        self.candidatos = []
        # Conteos globales del edificio (Punto 1 y 4)
        self.conteo_cabina_global = 0 
        self.votos_por_candidato = {} 

    def agregar_mesa(self, mesa):
        self.mesas[mesa.id_mesa] = mesa

    def cargar_censo_jec(self, lista_votantes):
        """
        Simula la carga de la JEC un mes antes.
        Reparte a los votantes en sus mesas correspondientes.
        """
        for v in lista_votantes:
            if v.mesa_id in self.mesas:
                self.mesas[v.mesa_id].censo_mesa[v.dni] = v

    def emitir_voto_cabina(self, dni, seleccion):
        """ Proceso de la Cabina (Punto 1) """
        # Buscamos al votante en todas las mesas del colegio
        votante = None
        for mesa in self.mesas.values():
            if dni in mesa.censo_mesa:
                votante = mesa.censo_mesa[dni]
                break
        
        if not votante or votante.ha_votado_en_cabina:
            return "Error: Votante no encontrado o ya votó."

        # Sumar al conteo del COLEGIO (Punto 1)
        self.conteo_cabina_global += 1
        
        # Lógica de selección
        if seleccion in self.votos_por_candidato:
            self.votos_por_candidato[seleccion] += 1
        
        votante.ha_votado_en_cabina = True
        return f"Imprimiendo... Acuda a la Mesa {votante.mesa_id}."