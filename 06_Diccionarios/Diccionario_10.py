clientes = {}

while True:
    print("\n--- MENÚ DE GESTIÓN DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    
    opcion = input("Elige una opción (1-6): ")

    if opcion == '1':
        # Añadir cliente
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        es_preferente = input("¿Es cliente preferente? (S/N): ").lower() == 's'
        
        # Se crea el diccionario interno y se guarda en el principal
        datos_cliente = {
            'nombre': nombre,
            'dirección': direccion,
            'teléfono': telefono,
            'correo': correo,
            'preferente': es_preferente
        }
        clientes[nif] = datos_cliente
        print(f"✅ Cliente {nombre} añadido correctamente.")

    elif opcion == '2':
        # Eliminar cliente por DNI
        nif = input("Introduce el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
            print(f"🗑️ Cliente con NIF {nif} eliminado.")
        else:
            print("❌ El NIF introducido no existe.")

    elif opcion == '3':
        # Mostrar un cliente específico
        nif = input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print(f"\nDatos del cliente {nif}:")
            for clave, valor in clientes[nif].items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print("❌ Cliente no encontrado.")

    elif opcion == '4':
        # Listar todos los clientes
        print("\n--- LISTA DE TODOS LOS CLIENTES ---")
        for nif, datos in clientes.items():
            print(f"NIF: {nif} - Nombre: {datos['nombre']}")

    elif opcion == '5':
        # Listar clientes preferentes
        print("\n--- LISTA DE CLIENTES PREFERENTES ---")
        for nif, datos in clientes.items():
            if datos['preferente']:
                print(f"NIF: {nif} - Nombre: {datos['nombre']}")

    elif opcion == '6':
        print("Saliendo del programa...")
        break

    else:
        print("⚠️ Opción no válida. Inténtalo de nuevo.")