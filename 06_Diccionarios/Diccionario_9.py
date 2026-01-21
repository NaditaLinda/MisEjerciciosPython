facturas = {}
cobrado = 0.0

while True:
    # Menú
    print("\n--- GESTIÓN DE FACTURAS ---")
    opcion = input("¿Qué quieres hacer? (Añadir / Pagar / Terminar): ").strip().lower()

    # Lógica para agregar facturas
    if opcion == "añadir":
        num_factura = input("Introduce el número de factura: ")
        coste = float(input(f"Introduce el coste de la factura {num_factura}: ").replace(",", "."))
        facturas[num_factura] = coste
        print(f"✅ Factura {num_factura} añadida.")

    # Lógica de pagos
    elif opcion == "pagar":
        num_factura = input("Introduce el número de la factura que se ha pagado: ")
        if num_factura in facturas:
            # Sumo el valor al total cobrado y la elimino del diccionario
            cobrado += facturas[num_factura]
            del facturas[num_factura]
            print(f"💰 Factura {num_factura} marcada como pagada.")
        else:
            print("❌ Esa factura no existe en el sistema.")

    elif opcion == "terminar":
        print("Cerrando el sistema de gestión...")
        break
    
    else:
        print("⚠️ Opción no válida. Por favor, elige Añadir, Pagar o Terminar.")

    pendiente = sum(facturas.values())
    print("-" * 30)
    print(f"Cantidad cobrada hasta el momento: {cobrado:.2f} €")
    print(f"Cantidad pendiente de cobro: {pendiente:.2f} €")
    print("-" * 30)