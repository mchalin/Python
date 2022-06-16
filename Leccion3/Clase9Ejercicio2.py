# Calcular la suma de N primeros números

cant = int(input("Ingrese la cantidad de nros a sumarse: "))
suma = 0
# Le pusimos cantidad + 1 para q no cuente el 0 en el rango
for i in range(cant+1):
    suma += i
print(f"La suma es: {suma}")