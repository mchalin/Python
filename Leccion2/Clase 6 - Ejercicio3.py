"""
Ejercicio 3
Intercambiar el valor de dos variables.
Por ejemplo:
a = 10 -> a = 5
b = 5  -> b = 10
"""
a = input("Ingrese un valor para la variable a: ")
b = input("Ahora ingrese un valor para la variable b: ")

temp = a
a = b
b = temp

print("Los nuevos valores son: ")
print("a: " + a)
print("b: " + b)
