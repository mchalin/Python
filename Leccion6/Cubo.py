class Cubo:
    """
    Crear una clase llamada Cubo, debe tener 3 atributos, ancho, alto y profundidad.
    El nombre del metodo sera calcular_volumen utilizando la formula:
    volumen = alto * ancho * profundidad
    Estos datos deben ser ingresados por el usuario, los objetos deben ser tres.
    """

    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.alto * self.ancho * self.profundidad


cubo1 = Cubo(int(input('Ingrese el alto del cubo1: ')),
             int(input('Ingrese el ancho del cubo1: ')),
             int(input('Ingrese la profundidad del cubo1: ')))
print(f'El volumen del cubo1 es: {cubo1.calcular_volumen()}')

cubo2 = Cubo(int(input('Ingrese el alto del cubo2: ')),
             int(input('Ingrese el ancho del cubo2: ')),
             int(input('Ingrese la profundidad del cubo2: ')))
print(f'El volumen del cubo2 es: {cubo2.calcular_volumen()}')

cubo3 = Cubo(int(input('Ingrese el alto del cubo3: ')),
             int(input('Ingrese el ancho del cubo3: ')),
             int(input('Ingrese la profundidad del cubo3: ')))
print(f'El volumen del cubo3 es: {cubo3.calcular_volumen()}')