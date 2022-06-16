# Escribí un programa que solicite al usuario una letra y, si es una vocal, 
# muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, 
# informarle que no se puede procesar el dato.

# Ejemplo de ejecución:

# Letra: o
# Es vocal

letra = input("Ingrese una letra: ")
if len(letra) > 1:
    print("Ingreso más de un caracter. No se puede procesar el dato.")
elif (letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u"):
    print("Ingresó una vocal")
else:
    print("El caracter ingresado no es una vocal.")
