class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos, altura y base.
    El nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura
    Estos datos deben ser ingresados por el usuario, los objetos deben ser tres.
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


rectangulo1 = Rectangulo(int(input('Ingrese altura del primer rectángulo: ')),
                         int(input('Ingrese base del primer rectángulo: ')))
print(f'El área de rectangulo1 es: {rectangulo1.calcular_area()}')

rectangulo2 = Rectangulo(int(input('Ingrese altura del segundo rectángulo: ')),
                         int(input('Ingrese base del segundo rectángulo: ')))
print(f'El área de rectangulo2 es: {rectangulo2.calcular_area()}')

rectangulo3 = Rectangulo(int(input('Ingrese altura del tercer rectángulo: ')),
                         int(input('Ingrese base del tercer rectángulo: ')))
print(f'El área de rectangulo3 es: {rectangulo3.calcular_area()}')
