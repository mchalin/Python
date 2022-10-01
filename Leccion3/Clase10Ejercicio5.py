# Calcular el factorial de un número mayor o igual a 0.

print("Calcular el factorial de un número mayor o igual a 0.")
print()
num = int(input("Ingrese un número: "))
factorial = 1
bucle = 1
while bucle == 1:
    if num >= 0:
        for i in range(num):
            factorial *= i+1
        bucle = 0
    else:
        num = int(input("Ingrese un número mayor o igual a 0: "))
print()
print(f"El factorial de {num} es: {factorial}")