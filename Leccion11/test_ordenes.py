from Orden import Orden
from Producto import Producto

producto1 = Producto('Remera', 2000.00)
producto2 = Producto('Pantalon', 5000.00)
print(producto1)
print(producto2)
productos1 = [producto1, producto2]  # Lista de productos
orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
print(orden1)
print(f'El monto total de la orden 1 es: {orden1.calcular_total()}')
orden2 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
print(orden2)
producto3 = Producto('Lapiz', 200.00)
producto4 = Producto('Lapicera', 300.00)
productos2 = [producto3, producto4, producto1]
orden3 = Orden(productos2)
print(orden3)

orden3.agregar_producto(producto2)
print(orden3)