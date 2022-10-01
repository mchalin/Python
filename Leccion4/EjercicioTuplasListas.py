# Ejercicio 1
# Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
# Ejemplo de ejecucion: 0,3,6,9
ejercicio = []
for i in range(11):
    if i % 3 == 0:
        ejercicio.append(i)
print("Ejercicio 1: ", ejercicio)
ejercicio.clear()

# Ejercicio 2
# Crear un rango de numeros de 2 a 6 e imprimirlos
# Ejemplo de ejecucion: 2,3,4,5,6
for i in range(2, 7):
    ejercicio.append(i)
print("Ejercicio 2: ", ejercicio)
ejercicio.clear()

# Ejercicio 3
# Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecucion: 3,5,7,9

for i in range(3, 11, 2):
    ejercicio.append(i)
print("Ejercicio 3: ", ejercicio)
print()

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []
for dato in tupla:
    if dato < 5:
        lista.append(dato)

print("Ejercicio 4 (tupla): ", lista)