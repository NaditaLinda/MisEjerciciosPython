import urllib.request

def contar_palabras_url():
    # Ejemplo de prueba: https://www.gutenberg.org/files/11/11-0.txt (Alicia en el país de las maravillas)
    url = input("Introduce la URL del archivo de texto (.txt): ").strip()

    try:
        print(f"Conectando a {url}...")
        with urllib.request.urlopen(url) as respuesta:
            
            # Lectura y decodificación
            # Paso los datos de bytes a texto (str)
            contenido_bytes = respuesta.read()
            contenido_texto = contenido_bytes.decode('utf-8')
            
            # Cuento las palabras
            # split() divide el texto por espacios, saltos de línea y tabuladores
            palabras = contenido_texto.split()
            numero_palabras = len(palabras)
            
            print(f"\n--- Resultado del Análisis ---")
            print(f"El archivo contiene aproximadamente {numero_palabras} palabras.")

    except urllib.error.URLError as e:
        print(f"Error de conexión: No se pudo acceder a la URL. {e.reason}")
    except UnicodeDecodeError:
        print("Error: El archivo no parece estar en formato UTF-8.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    contar_palabras_url()