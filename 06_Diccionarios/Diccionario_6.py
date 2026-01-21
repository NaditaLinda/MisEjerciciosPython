persona = {}

print("--- Registro de Usuario ---")
print("(Escribe 'salir' en el nombre del dato para terminar)\n")

while True:
    clave = input("¿Qué dato quieres introducir? (ej: Nombre, Edad, Email): ")
    
    if clave.lower() == "salir":
        break
        
    valor = input(f"Introduce el valor para '{clave}': ")
    
    persona[clave] = valor
    
    print("\n📊 Información actual en el sistema:")
    print(persona)
    print("-" * 30)

print("\n✅ Proceso finalizado. Diccionario resultante:")
print(persona)