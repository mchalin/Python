# Sistema de calificaciones
# El objetivo del programa sera crear un sistema de calificaciones de la siguiente manera:
# Le pedimos al usuario que ingrese un valor del 0 al 10
# Luego si ingreso 9 o 10 imprimos A
# entre 8 y menor a 9 imprimos B
# entre 7 y menor a 8 imprimos C
# entre 6 y menor a 7 imprimos D
# entre 0 y menor a 6 imprimos F
# De lo contrario el valor ingresado es incorrecto

calificacion = int(input("Ingrese un valor del 0 al 10: "))
if 9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion < 9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif 0 <= calificacion < 6:
    print("F")
else:
    print("Valor incorrecto")
