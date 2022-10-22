class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase en Python
    Vamos a hacer en esta clase algunas operacion de: suma, resta, multiplicacion y mas
    """

    def __init__(self, nro1, nro2):
        self.nro1 = nro1
        self.nro2 = nro2

    # Método para sumar
    def sumar(self):
        return self.nro1 + self.nro2

    # Método para restar
    def restar(self):
        return self.nro1 - self.nro2

    # Método para multiplicar
    def multiplicar(self):
        return self.nro1 * self.nro2

    # Método para dividir
    def dividir(self):
        return self.nro1 / self.nro2


aritmetica1 = Aritmetica(7, 9)  # le pasamos los argumentos para los operandos
# print(aritmetica1.sumar())
# print(aritmetica1.restar())
# print(aritmetica1.multiplicar())
# print(aritmetica1.dividir())

print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.restar()}')
print(f'La multiplicacion de los números es: {aritmetica1.multiplicar()}')
print(f'La division de los números es: {aritmetica1.dividir():.2f}')  # Imprime solo dos decimales del numero flotante
