import os

FICHERO = "listin.txt"

def crear_listin():
    """Crea el fichero si no existe."""
    if not os.path.exists(FICHERO):
        with open(FICHERO, "w", encoding="utf-8") as f:
            pass  # Crea el archivo vacío
        print(f"Archivo '{FICHERO}' creado con éxito.")

def consultar_cliente():
    nombre_buscar = input("Introduce el nombre del cliente a consultar: ").strip().lower()
    encontrado = False
    try:
        with open(FICHERO, "r", encoding="utf-8") as f:
            for linea in f:
                nombre, telefono = linea.strip().split(",")
                if nombre.lower() == nombre_buscar:
                    print(f"El teléfono de {nombre} es: {telefono}")
                    encontrado = True
                    break
        if not encontrado:
            print("Cliente no encontrado.")
    except FileNotFoundError:
        print("El listín no existe todavía.")

def anadir_cliente():
    nombre = input("Nombre del nuevo cliente: ").strip()
    telefono = input("Teléfono del cliente: ").strip()
    with open(FICHERO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{telefono}\n")
    print(f"Cliente {nombre} añadido correctamente.")

def eliminar_cliente():
    nombre_borrar = input("Nombre del cliente a eliminar: ").strip().lower()
    lineas_finales = []
    encontrado = False
    
    try:
        with open(FICHERO, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            
        for linea in lineas:
            nombre, telefono = linea.strip().split(",")
            if nombre.lower() == nombre_borrar:
                encontrado = True
            else:
                lineas_finales.append(linea)
        
        if encontrado:
            with open(FICHERO, "w", encoding="utf-8") as f:
                f.writelines(lineas_finales)
            print(f"Cliente '{nombre_borrar}' eliminado.")
        else:
            print("El cliente no existe en el listín.")
    except FileNotFoundError:
        print("No se puede eliminar porque el fichero no existe.")

# Menú con las funciones
def menu():
    crear_listin()
    while True:
        print("\n--- GESTIÓN DE LISTÍN ---")
        print("1. Consultar cliente")
        print("2. Añadir cliente")
        print("3. Eliminar cliente")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            consultar_cliente()
        elif opcion == "2":
            anadir_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()