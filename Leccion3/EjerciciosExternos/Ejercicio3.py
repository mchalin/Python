# Escribí un programa que solicite al usuario dos números y los almacene en dos variables.
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número,
# el cual se debe almacenar en una nueva variable.
# Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número
# por el resultado de la suma anterior.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
suma = num1 + num2
print(f"La suma de {num1} + {num2} es igual a: {suma}")
num3 = int(input("Ingrese un tercer número: "))
print(f"El producto de {suma} y {num3} es igual a {suma * num3}")
