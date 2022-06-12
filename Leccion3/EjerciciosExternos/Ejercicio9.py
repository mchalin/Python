# Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
# A continuación, mostrar en pantalla la primera letra del texto ingresado.
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres
# que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4)
# y almacenar este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
#
# Ejemplo de ejecución:
#
# Ingresá un texto: En un lugar de La Mancha, de cuyo nombre no quiero acordarme...
# El carácter en primer lugar es: E
# Ingresá un número positivo menor a 63
# 7
# El carácter en esa posición es: u
texto = input("Ingrese un texto: ")
print(f"El caracter en primer lugar es: {texto[0]}")
posicion = int(input(f"Ingresa un número positivo menor a {len(texto)}: "))
print(f"El carácter en esa posición es: {texto[posicion]}")
