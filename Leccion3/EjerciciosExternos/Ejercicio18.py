# Escribí un programa que solicite al usuario el ingreso de dos números diferentes 
# y muestre en pantalla al mayor de los dos.
 
# Ejemplo de ejecución:

# Un número: 592
# Otro número distinto: 1726
# 1726 es mayor

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num1 > num2:
    print(f"{num1} es mayor")
else: 
    print(f"{num2} es mayor")