import json

def generar_archivo_preguntas():
    # Lista base de preguntas reales
    banco_preguntas = [
        {"pregunta": "¿Qué lenguaje creó Guido van Rossum?", "respuesta": "python", "tema": "Programación"},
        {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "paris", "tema": "Geografía"},
        {"pregunta": "¿En qué año se lanzó el primer iPhone?", "respuesta": "2007", "tema": "Tecnología"},
        {"pregunta": "¿Cuál es el símbolo químico del Oro?", "respuesta": "au", "tema": "Ciencia"},
        {"pregunta": "¿Quién pintó la Mona Lisa?", "respuesta": "da vinci", "tema": "Arte"}
    ]

    # Para llegar a 1000, podemos automatizar preguntas matemáticas o de relleno
    # mientras consigues un dataset más grande.
    for i in range(1, 996):
        num1 = i
        num2 = 5
        banco_preguntas.append({
            "pregunta": f"Calcula mentalmente: ¿Cuánto es {num1} + {num2}?",
            "respuesta": str(num1 + num2),
            "tema": "Matemáticas"
        })

    # Guardar en el archivo JSON
    with open("preguntas.json", "w", encoding="utf-8") as f:
        json.dump(banco_preguntas, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Archivo preguntas.json creado con {len(banco_preguntas)} preguntas.")

if __name__ == "__main__":
    generar_archivo_preguntas()
    