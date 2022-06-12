# Escribí un programa que solicite al usuario que ingrese
# cuántos shows musicales ha visto en el último año y almacene ese número en una variable.
# A continuación mostrar en pantalla un valor de verdad (True o False)
# que indique si el usuario ha visto más de 3 shows.
#
# Ejemplo de ejecución:
#
# Shows vistos en el último año: 3
# False

vistos = int(input("Ingrese la cantidad de shows vistos el último año: "))
valorVerdad = vistos > 3
print(f"El usuario vio mas de 3 shows?: {valorVerdad}")
