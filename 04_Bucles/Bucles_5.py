while True:
    try:
        cantidad = float(input("Cantidad a invertir (€): ").replace(',', '.'))
        interes = float(input("Interés anual (%): ").replace(',', '.'))
        años = int(input("Número de años: "))

        if cantidad <= 0 or interes <= 0 or años <= 0:
            print("Error: Todos los valores deben ser mayores que cero.")
        else:
            print(f"\n--- Proyección de Inversión ---")
            
            capital = cantidad
            
            for i in range(1, años + 1):
                capital *= (1 + interes / 100)
                
                print(f"Año {i}: {capital:.2f} €")
            
            break

    except ValueError:
        print("Error: Introduce valores numéricos válidos (ej: 1000, 3.5, 5).")