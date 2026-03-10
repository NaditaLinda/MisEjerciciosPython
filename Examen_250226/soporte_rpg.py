class Preguntero:
    def __init__(self, archivo_json="preguntas.json"):
        self.archivo = archivo_json
        self.preguntas = self._cargar_preguntas()

    def _cargar_preguntas(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Archivo de preguntas no encontrado. Usando preguntas de emergencia.")
            return [{"pregunta": "2 + 2", "respuesta": "4"}]

    def lanzar_desafio(self, personaje):
        print("\n" + "═"*40)
        print("📜 DESAFÍO DE CULTURA GENERAL")
        print("═"*40)
        
        reto = random.choice(self.preguntas)
        print(f"Pregunta: {reto['pregunta']}")
        
        intentos = 1
        while intentos > 0:
            res = input("Tu respuesta: ").strip().lower()
            if res == reto['respuesta']:
                print("✨ ¡Sabiduría ancestral demostrada!")
                self._dar_recompensa(personaje)
                return True
            else:
                print("❌ Respuesta incorrecta.")
                intentos -= 1
        return False

    def _dar_recompensa(self, personaje):
        recompensa = random.choice(["ATK", "MP", "HP"])
        if recompensa == "ATK":
            personaje._ataque_base += 5
            print(f"⚔️ ¡Tu ataque sube a {personaje._ataque_base}!")
        elif recompensa == "MP":
            personaje._mana_max += 25
            personaje._mana_actual = personaje._mana_max
            print(f"🧪 ¡Tu maná máximo sube a {personaje._mana_max}!")
        elif recompensa == "HP":
            personaje._vida_max += 25
            personaje._vida_actual = personaje._vida_max
            print(f"❤️ ¡Tu salud máxima sube a {personaje._vida_max}!")

evento = Preguntero()