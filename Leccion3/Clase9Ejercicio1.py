# Diseñar un programa que ingresado un año, nos devuelva por
# consola si es un año bisiesto o no, repetir la accion hasta que el
# usuario lo decida.
print("Comprobamos que año es bisiesto.")
bucle = 1
while bucle == 1:
    anio = int(input("Ingrese un año: "))
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
    print()
    bucle = int(input("Ingrese el nro 1 para repetir consulta: "))
