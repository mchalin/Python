# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10,
# luego modificar los elementos de la lista multiplicandolos por un número ingresado por el usuario

lista = list(range(1,11))

print(f"Lista original: {lista}")

nro_usuario = int(input("Ingrese un número para multiplicar la lista: "))
for indice, i in enumerate(lista):
    lista[indice] *= nro_usuario

print(f"Lista modificada (*{nro_usuario}): \n{lista}")