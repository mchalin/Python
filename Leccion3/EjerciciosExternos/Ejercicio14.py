# Escribí un programa que, dada una cadena de texto por el usuario, 
# imprima True si la cantidad de caracteres en la cadena es un número impar, 
# o False si no lo es.
# Ejemplo de ejecución:

# Ingresá una frase: Era el mejor de los tiempos, era el peor de los tiempos.
# True

texto = input("Ingresa una frase: ")
print((len(texto) % 2 == 0))