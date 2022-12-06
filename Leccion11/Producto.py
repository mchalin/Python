class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'Producto: [ID PRODUCTO: {self._id_producto} NOMBRE: {self._nombre} PRECIO: {self._precio}]'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio


if __name__ == '__main__':
    producto1 = Producto('Remera', 2000.00)
    producto2 = Producto('Pantalon', 5000.00)
    print(producto1)
    print(producto2)
