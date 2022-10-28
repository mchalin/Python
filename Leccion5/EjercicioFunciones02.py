# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función
# y regresar como resultado la multiplicación de todos los valores pasados como argumentos

def multiplicar_valores(*args):
    resultado = 1  # Inicializamos el contador, 1 no influye en la multiplicacion
    for numero in args:
        resultado *= numero
    return resultado


print(multiplicar_valores(9, 8, 7, 6))  # argumentos
