# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta
# y la cantidad de litros de combustible que consumió durante ese recorrido.
# Mostrar el consumo de combustible por kilómetro.

kms = float(input("Ingrese cantidad de kilómetros recorridos: "))
lts = float(input("Ingrese la cantidad de libros de nafta que consumió: "))
consumo = lts / kms
print(f"La motocicleta consume {consumo} lts de nafta por litro recorrido.")