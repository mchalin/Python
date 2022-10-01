# Ingresar N enteros, visualizar la suma de los nros pares de la lista,
# cuantos numeros pares existen y cual es el promedio de los numeros impares

cantNros = int(input("Ingrese cuantos números utilizará en el ejercicio: "))
contadorPares = 0
contadorImpares = 0
sumaPares = 0
sumaImpares = 0

for i in range(cantNros):
    nro = int(input("Ingrese un número entero: "))
    if nro % 2 == 0:
        contadorPares += 1
        sumaPares += nro
    else:
        contadorImpares += 1
        sumaImpares += nro
print(f"""
Suma de nros pares:         {sumaPares if contadorPares != 0 else "No se ingresaron nros pares."}
Conteo de nros pares:       {contadorPares if contadorPares != 0 else "No se ingresaron nros pares."}
Promedio de nros impares:   {(sumaImpares/contadorImpares) if contadorImpares != 0 else "No se ingresaron nros impares."} 
""")
