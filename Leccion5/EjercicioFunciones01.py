# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo numéricos,
# utilizando argumentos variables *args como parametro de la función
# y agregar como resultado la suma de todos los valores pasados como argumentos.

def sumar_valor(*args):  # Parámetros indefinidos
    resultado = 0
    for valor in args:  # iteramos
        resultado += valor
    return resultado


print(sumar_valor(1, 2, 3, 4, 5))
