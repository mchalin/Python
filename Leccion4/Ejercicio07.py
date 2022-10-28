# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe generar un número aleatorio entre 1 - 100,
# y luego ir pidiendo números indicando "es mayor" o "es menor" según cuan sea mayor o menor con respecto a N.
# El proceso termina cuando el usuario acierta y allí se debe mostrar el número de intentos.
import random

print("Adivina el número aleatorio.")
nro = random.randint(0, 100)
# print(nro)
contador = 1
nro_usuario = int(input("Ingrese un número: "))
while nro != nro_usuario:
    contador += 1
    if nro > nro_usuario:
        nro_usuario = int(input("El nro es demasiado bajo, intenta nuevamente: "))
    else:
        nro_usuario = int(input("El nro es demasiado alto, intenta nuevamente: "))

print(f'Felicidades! Adivinaste el nro secreto luego de {contador} intentos.')
