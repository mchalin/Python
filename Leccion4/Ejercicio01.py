# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar la lista con el bucle for.
# Los elementos deben mostrarse con la siguiente forma
# 1-2-3-4-5-....-50

# lista = []
# for i in range(1,51):
#     lista.append(i)

lista = list(range(1, 51))

print("Imprimimos la lista:")
for item in lista:
    print(item, end="-")
