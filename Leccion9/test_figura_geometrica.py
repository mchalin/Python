from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado = Cuadrado(5, "Amarillo")

print(cuadrado.ancho)
print(cuadrado.alto)
print(f'Calculo del area: {cuadrado.calcular_area()}')

# MRO = Method Resolution Order

print(Cuadrado.mro())

print(cuadrado)
rectangulo1 = Rectangulo(10, 5, "verde")

print(f'Calculo del area: {rectangulo1.calcular_area()}')
print(rectangulo1)
