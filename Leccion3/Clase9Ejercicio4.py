# Suponga q se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
# Realizar un algoritmo para calcular la calificacion promedio
# y la calificacion mas baja de todo el grupo

suma = 0
laNotaMasBaja = 10000
for i in range(10):
    calificacion = int(input(f"Ingrese la calificacion del alumno {i + 1}: "))
    if calificacion < laNotaMasBaja:
        laNotaMasBaja = calificacion
    suma += calificacion
promedio = suma / 10
print(f'''
    La calificación mas baja es:        {laNotaMasBaja}
    El promedio de los 10 alumnos es:   {promedio}
''')