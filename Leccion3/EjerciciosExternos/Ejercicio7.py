# Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable.
#  A continuación, mostrar el resultado final en pantalla.
#
# Ejemplo de ejecución:
#
# Ingresá un número: 260
# Descontando el 15% queda: 221.0
num = float(input("Ingrese un número: "))
num -= num * 0.15
print(f"Con el descuento del 15% queda asi: {num}")
