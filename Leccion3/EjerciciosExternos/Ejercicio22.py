# Escribí un programa que permita saber si un año es bisiesto.
# Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
# excepto que también sea divisible por 400.
 
# Ejemplo de ejecución:

# Año: 2020
# Bisiesto

anio = int(input("Ingrese un año: "))
if anio % 4 == 0:
    print("Divisible por 4")
    if anio % 400 == 0 :
        print(f"El año {anio} es bisiesto!")
