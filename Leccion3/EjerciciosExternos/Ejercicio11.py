# Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números
# donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero)
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
# Ejemplo de ejecución:
# Fecha en formato DDMMAAAA: 16112017
# 16 / 11 / 2017

fecha = int(input("Ingrese una fecha en formato DDMMAAAA: "))
anio = fecha % 10000
fecha //= 10000
mes = fecha % 100
fecha //= 100
print(fecha,"/",mes,"/",anio)
