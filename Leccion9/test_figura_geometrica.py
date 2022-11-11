from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print("Creacion de objeto Clase Cuadrado".center(50, "_"))
cuadrado = Cuadrado(5, "Amarillo")
print(f'Ancho: {cuadrado.ancho}')
print(f'Alto: {cuadrado.alto}')
print(f'Color: {cuadrado.color}')
print(f'Calculo del area: {cuadrado.calcular_area()}')

# MRO = Method Resolution Order
print(f'\nMethod Resolution Order: \n{Cuadrado.mro()}\n')
print(cuadrado)

print("Creacion de objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(3, 9, "verde")
rectangulo1.ancho = 23 # No pasa la validacion, no modifica nada en el objeto EDIT, tiene validacion, da error
print(f'Calculo del area: {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica() # No se puede instanciar por ser clase abstracta