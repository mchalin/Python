# Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
#
# Ejemplo de ejecución:
#
# Primer número: 8.5
# Segundo número: 10
# Tercer número: 5.5
# El promedio de los tres es 8.0

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ahora ingrese el segundo número: "))
num3 = float(input("Por último, el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2}, {num3} es: {promedio}")
