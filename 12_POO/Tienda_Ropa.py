class Producto:
    def __init__(self, idProducto, nombre, talla, color, precio, stock):
        self.idProducto = idProducto
        self.nombre = nombre
        self.talla = talla
        self.color = color
        self.precio = precio
        self.stock = stock

    def mostrarInfo(self):
        print(f"Producto: {self.nombre} | Precio: {self.precio}€ | Stock: {self.stock}")

    def actualizarStock(self, cantidad):
        self.stock += cantidad

    def aplicarDescuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)
        return self.precio

class Tienda:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.listaProductos = []
        self.listaEmpleados = []

    def agregarProducto(self, producto):
        self.listaProductos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")

    def listarProductos(self):
        print(f"\n--- Inventario de {self.nombre} ---")
        for p in self.listaProductos:
            p.mostrarInfo()

class Cliente:
    def __init__(self, idCliente, nombre, email, telefono):
        self.idCliente = idCliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.historial = []

    def registrarse(self):
        print(f"Cliente {self.nombre} registrado con éxito.")

    def realizarCompra(self, venta):
        self.historial.append(venta)
        print(f"Compra {venta.idVenta} añadida al historial de {self.nombre}.")

    def verHistorialCompras(self):
        print(f"Historial de {self.nombre}: {len(self.historial)} compras realizadas.")

class Empleado:
    def __init__(self, idEmpleado, nombre, cargo, salario):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def registrarVenta(self, venta):
        print(f"Venta {venta.idVenta} registrada por {self.nombre}.")

class Venta:
    def __init__(self, idVenta, fecha):
        self.idVenta = idVenta
        self.fecha = fecha
        self.productos = []
        self.total = 0.0

    def agregarProducto(self, producto):
        if producto.stock > 0:
            self.productos.append(producto)
            producto.actualizarStock(-1)
            self.total += producto.precio
        else:
            print(f"Sin stock para {producto.nombre}")

    def calcularTotal(self):
        return self.total

class Pago:
    def __init__(self, idPago, tipoPago, monto):
        self.idPago = idPago
        self.tipoPago = tipoPago
        self.monto = monto

    def procesarPago(self):
        print(f"Procesando pago de {self.monto}€ vía {self.tipoPago}...")
        return True
    
# --- Ejemplo de uso para probar que funciona ---
    
# 1. Creamos objetos
vendedor = Empleado(101, "Ana", "Vendedora", 1200)
comprador = Cliente(501, "Carlos", "carlos@mail.com", "600000000")
prenda = Producto(1, "Chaqueta", "L", "Negro", 59.95, 10)

# 2. Iniciamos una venta
ticket = Venta(2026, "17-02-2026")
ticket.agregarProducto(prenda)

# 3. Finalizamos procesos
vendedor.registrarVenta(ticket)
comprador.realizarCompra(ticket)

print(f"Total a pagar: {ticket.calcularTotal()}€")