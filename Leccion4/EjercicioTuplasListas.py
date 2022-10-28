import math

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []
for dato in tupla:
    if dato < 5:
        lista.append(dato)

print("Ejercicio 4 (tupla): ", lista)
print()

# Importamos la clase math
# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un número positivo
numero = int(input("Sacar raíz cuadrada \nIngrese un número: "))
while numero < 0:
    print("Error. Debe ser un número positivo.")
    numero = int(input("Ingrese un número: "))
raiznumero = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiznumero:.2f}")
