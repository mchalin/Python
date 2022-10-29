class Vehiculo:
    """
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Auto y Bicicleta,
    las cuales heredan de la clase padre Vehiculo.
    La clase padre debe tener los siguientes atributos y metodos.

    Vehiculo (Clase padre)
    -Atributos (color, ruedas)
    -Metodos (__init__(color, ruedas) y __str__())

    Auto (Clase hija de Vehiculo)
    -Atributos (velocidad (km/hr))
    -Metodos (__init__(color, ruedas, velocidad) y __str__())

    Bicicleta (Clase hija de Vehiculo)
    -Atributos (tipo (urbana, montaña, etc))
    -Metodos (__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase.
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo -> Color: {self.color} Ruedas: {self.ruedas}'


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Auto -> Velocidad: {self.velocidad}km/hr \nHija de: {super().__str__()}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta -> Tipo: {self.tipo} \nHija de: {super().__str__()}'


vehiculo1 = Vehiculo('Marron', 4)
print(vehiculo1)
print()

vehiculo2 = Auto('Gris', 4, 110)
print(vehiculo2)
print()

vehiculo3 = Bicicleta('Roja', 2, 'Mountain bike')
print(vehiculo3)
