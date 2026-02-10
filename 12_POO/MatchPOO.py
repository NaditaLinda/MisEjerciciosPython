from datetime import datetime

# Clase Persona (Base)
class Persona:
    def __init__(self, nombre, edad: int, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad} | Ciudad: {self.ciudad}")

# Clase Interes (Independiente)
class Interes:
    def __init__(self, nombre_interes, categoria):
        self.nombre_interes = nombre_interes
        self.categoria = categoria

    def mostrar_interes(self):
        print(f"[{self.categoria}] {self.nombre_interes}")

# Clase Perfil (Relacionada con Usuario e Interes)
class Perfil:
    def __init__(self, descripcion, profesion, altura: float, fumador: bool):
        self.descripcion = descripcion
        self.profesion = profesion
        self.altura = altura
        self.fumador = fumador
        self.intereses = [] # Lista de objetos Interes

    def mostrar_descripcion(self):
        fuma = "Sí" if self.fumador else "No"
        print(f"Perfil: {self.descripcion}\nTrabajo: {self.profesion} | Altura: {self.altura}m | Fumador: {fuma}")

# Clase Usuario (Hereda de Persona)
class Usuario(Persona):
    def __init__(self, nombre, edad, ciudad, email, perfil: Perfil):
        super().__init__(nombre, edad, ciudad)
        self.email = email
        self.perfil = perfil
        self.mensajes_enviados_hoy = 0

    def mostrar_perfil(self):
        self.mostrar_datos()
        self.perfil.mostrar_descripcion()

    def puede_enviar_mensaje(self):
        # Lógica base, será sobrescrita por los hijos
        return True

# Usuario Gratuito
class UsuarioGratuito(Usuario):
    def enviar_mensaje(self, destinatario, texto):
        if self.mensajes_enviados_hoy < 2: # Límite de 2 mensajes
            nuevo_mensaje = Mensaje(texto, self, destinatario)
            self.mensajes_enviados_hoy += 1
            return nuevo_mensaje
        else:
            print(f"Límite alcanzado para {self.nombre}. Pásate a Premium.")
            return None

# Usuario Premium
class UsuarioPremium(Usuario):
    def __init__(self, nombre, edad, ciudad, email, perfil, tipo_suscripcion, likes):
        super().__init__(nombre, edad, ciudad, email, perfil)
        self.tipo_suscripcion = tipo_suscripcion
        self.likes_disponibles = likes

    def enviar_mensaje(self, destinatario, texto):
        # Sin límite de mensajes
        nuevo_mensaje = Mensaje(texto, self, destinatario)
        self.mensajes_enviados_hoy += 1
        return nuevo_mensaje

    def dar_like(self):
        if self.likes_disponibles > 0:
            self.likes_disponibles -= 1
            print(f"¡Like enviado! Te quedan {self.likes_disponibles}.")

# Clase Mensaje
class Mensaje:
    def __init__(self, texto, remitente, destinatario):
        self.texto = texto
        self.fecha = datetime.now()
        self.remitente = remitente
        self.destinatario = destinatario

    def mostrar_mensaje(self):
        print(f"[{self.fecha.strftime('%H:%M')}] De: {self.remitente.nombre} para {self.destinatario.nombre}: {self.texto}")

# Clase Match
class Match:
    def __init__(self, usuario1, usuario2):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.fecha_match = datetime.now()

    def mostrar_match(self):
        print(f"❤️ ¡MATCH! entre {self.usuario1.nombre} y {self.usuario2.nombre} el {self.fecha_match.strftime('%d/%m/%Y')}")