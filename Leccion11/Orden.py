from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)  # Para agregar nuevo producto

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f'Orden {self._id_orden} \nProductos: \n{productos_str}\nTotal: {self.calcular_total()}'


if __name__ == '__main__':
    producto1 = Producto('Remera', 2000.00)
    producto2 = Producto('Pantalon', 5000.00)
    print(producto1)
    print(producto2)
    productos1 = [producto1, producto2]  # Lista de productos
    orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
    print(orden2)
    producto3 = Producto('Lapiz', 200.00)
    producto4 = Producto('Lapicera', 300.00)
    productos2 = [producto3, producto4, producto1]
    orden3 = Orden(productos2)
    print(orden3)

