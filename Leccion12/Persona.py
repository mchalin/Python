class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):  # Puede recibir cualquier nombre
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):  # Resta (de substraction)
        return self.edad - other.edad


if __name__ == '__main__':
    persona1 = Persona('Maxi', 39)
    persona2 = Persona('Vale', 37)
    # persona1.__add__(persona2) # Sintaxis interna y automatica

    print(persona1 + persona2)  # Al realizar una suma, referencia la sobrecarga de operador suma (__add__)
    print(persona1 - persona2)
