# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
#       suma de nros pares del 2 al 30
#       suma = 240
print("Sumar números pares dentro de un rango.")
suma = 0
rango1 = int(input("Ingrese rango inferior: "))
rango2 = int(input("Ingrese rango superior: "))

for i in range(rango1, rango2 + 1):
    if i % 2 == 0:
        suma += i

print(f"La suma de los números pares en el rango ({rango1}:{rango2}) es: {suma}")
