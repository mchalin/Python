# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
print("Calcular el factorial de un número.")
num = int(input("Ingrese un número positivo: "))
factorial = 1
if num <= 0:
    print("Error. Debe ser un número positivo.")
else:
    for i in range(1,num+1):
        factorial *= i
print(f"El factorial de {num} es: {factorial}")