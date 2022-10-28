# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario ingrese un número 0, nuestro programa deja de insertar.
# Por último, mostrar los números de menor a mayor.
print("Haremos una lista con los números que ingrese el usuario. Se terminan de agregar al ingresar '0'.")
lista = []
num = int(input("Ingrese un número: "))
while num != 0:
    lista.append(num)
    num = int(input("Ingrese un número: "))

lista.sort()
print(f"La lista de números ordenados de menor a mayor: \n{lista}")