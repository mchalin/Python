# Escribí un programa que solicite al usuario el ingreso de dos palabras,
# las cuales se guardarán en dos variables distintas.
# A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio,
# más la segunda palabra. Mostrá este resultado en pantalla.
#
# Ejemplo de ejecución:
#
# Primera palabra: derribando
# Segunda palabra: muros
# derribando muros

palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

conca = palabra1 + " " + palabra2

print(f"La concatenación de las dos variables da como resultado: '{conca}'")