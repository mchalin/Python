"""
print("Cambiando valor a la misma variable, en Phyton son dinámicas")
# Variable tipo int
miVariable = 3
print(miVariable)
# Misma variable tipo string
miVariable = "Hola a todos"
print(miVariable)
# Misma variable tipo float
miVariable = 2.3
print(miVariable)
print()  # Linea en blanco
print("Mostrando valores literales de x, y, z")
x = 10
y = 2
z = x + y
# Imprime valores literales de variables
print(id(x))
print(id(y))
print(id(z))
print()  # Linea en blanco
# Variables tipo int, float, string y bool
print("Tipos de variables!")
x = 10
print(x)
print(type(x))
x = 12.45
print(x)
print(type(x))
x = "hola che"
print(x)
print(type(x))
x = False
print(x)
print(type(x))
print()  # Linea en blanco

# Manejo de cadenas (String)
print("Manejo de cadenas!")
miGrupoFavorito = "Radiohead"
comoSon = "Los mejores"
print("Mi Grupo favorito es:", miGrupoFavorito, comoSon)  # Se concatena automaticamente
numero1 = "7"
numero2 = "8"
print(numero1 + numero2)  # Como tipo string
print(int(numero1) + int(numero2))  # Pasa su valor a int
print()  # Linea en blanco

# Tipos booleanos
print("Datos booleanos")
miBooleano = 1 < 3
print(miBooleano)
if miBooleano:
    print("El valor es verdadero")
else:
    print("El resultado es falso")
print()  # Linea en blanco

# Procesar la entrada del usuario - funcion input
print("Entrada de datos..")
resultado = input("Digite un número: ")  # Regresa dato tipo String
print(resultado, "es de tipo", type(resultado))
print()  # Linea en blanco
# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)
print()  # Linea en blanco

# Clase 3
# Ejercicio 1: Califica tu día
# ¿Cómo estuvo tu día (1 al 10)?
# Mi día estuvo de: 10
# Hacer el código
# Debes hacerlo en PyCharm y también en el celular y en la terminal de Python...
print("Como estuvo tu dia?")
miDia = input("Ingresa un valor del 1 al 10..")
print()  # Linea en blanco
print("Mi dia estuvo de:", miDia)
print()  # Linea en blanco
# Ejercicio 2:
# Se solicita incluir la siguiente información acerca de un libro:
# titulo
# autor
# Debes imprimir la información en el siguiente formato:
# Proporciona el título:
# Proporciona el autor:
# <titulo> fue escrito por <autor>
titulo = input("Proporciona el título del libro: ")
autor = input("Proporciona el autor del libro: ")
print()  # Linea en blanco
print(titulo, "fue escrito por", autor)
print()  # Linea en blanco
# Clase 4 - Operadores
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
# print("Resultado de la suma:", suma)
print(f"El resultado de la suma es: {suma}")  # interpolacion
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicacion}")
division = operandoA / operandoB
print(f"El resultado de la división es: {division}")
division = operandoA // operandoB
print(f"El resultado de la división es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
print()  # Linea en blanco

# Clase 4, Ejercicio1
# Calcular área y perímetro de un rectángulo. Creando las variables alto (int) y ancho (int)

alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

miVariable3 = 10
print(miVariable3)

# Operadores de reasignación
miVariable3 += 1  # miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 -= 2  # miVariable3 = miVariable3 - 2
print(miVariable3)
miVariable3 *= 3  # miVariable3 = miVariable3 * 3
print(miVariable3)
miVariable3 /= 3  # miVariable3 = miVariable3 / 3
print(miVariable3)
print(type(miVariable3))
print()  # Linea en blanco

# Operadores de comparación
d = 4
b = 2
print(f"d: {d}")
print(f"b: {b}")
resultado = d == b  # Comprobamos si son iguales
print(f"Son iguales?: {resultado}")
resultado = d != b  # Comprobamos si son diferentes
print(f"Son diferentes?: {resultado}")
resultado = d > b  # Comprobamos si es mayor
print(f"La variable d es mayor que la variable b?: {resultado}")
resultado = d < b  # Comprobamos si es menor
print(f"La variable d es menor que la variable b?: {resultado}")
resultado = d >= b  # Comprobamos si es mayor o igual
print(f"La variable d es mayor o igual que la variable b?: {resultado}")
resultado = d <= b  # Comprobamos si es menor o igual
print(f"La variable d es menor o igual que la variable b?: {resultado}")
print()  # Linea en blanco

# Clase 4, Ejercicio2
# Número par o impar
numeroParOImpar = int(input("Ingrese un número a consultar si es par o impar: "))
print(f"El residuo de la división es: {numeroParOImpar % 2}")
if numeroParOImpar % 2 == 0:
    print(f"El número {numeroParOImpar} es par.")
else:
    print(f"El número {numeroParOImpar} es impar.")
print()  # Linea en blanco

# Clase 4, Ejercicio3
# Determinar si es mayor de edad

numeroMayorEdad = int(input("Ingrese la edad a consultar: "))
if numeroMayorEdad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
print()  # Linea en blanco

# Operadores lógicos
unBooleano = False
otroBooleano = True
resultado = unBooleano and otroBooleano  # Devuelve True si los dos son True
print(f"El resultado de {unBooleano} AND {otroBooleano} es: {resultado}")
resultado = unBooleano or otroBooleano  # Devuelve True si al menos hay un True en la consulta
print(f"El resultado de {unBooleano} OR {otroBooleano} es: {resultado}")
resultado = not unBooleano
print(f"Ahora probamos NOT en {unBooleano}: {resultado}")
print()  # Linea en blanco


# Clase 4, Ejercicio 4
# Valor dentro de un rango
numeroParaRango = int(input("Ingrese un número para consultar: "))
if numeroParaRango >= 0 and numeroParaRango <= 5:
    print(f"El número {numeroParaRango} está en el rango 0 a 5")
else:
    print(f"El número {numeroParaRango} no está en el rango 0 a 5")
print()  # Linea en blanco
"""
# # Clase 4, Ejercicio 5 (operador OR y NOT)
# # Puede asistir al juego de su hijo?
# # Verificamos si tiene vacaciones
# # Verificamos si tiene el dia libre
#
# tieneElDiaLibre = True
# tieneVacaciones = True
# if not (tieneVacaciones or tieneElDiaLibre):  # Cambiamos el resultado!!! con NOT
#     print("Tiene cosas que hacer")
# else:
#     print("Puede asistir al juego.")

# Clase 4, Ejercicio 6 (if elif else)
# Rango entre las edades 20 y 30 años
# Preguntar la edad al usuario
# Si la edad esta dentro de los 20 o 30 años, esta dentro del rango
# Combinamos los operadores and y or para saber si el usuario esta dentro del rango o no

# edadUsuario = int(input("Ingrese su edad por favor: "))
# veinti = 20 <= edadUsuario < 30 # Sintaxis simplificada del operador AND
# treinti = 30 <= edadUsuario < 40
#
# if veinti or treinti:
#     if veinti:
#         print(f'La edad ingresada es {edadUsuario}, estas dentro del rango de los 20\'0 años')
#     elif treinti:
#         print(f"La edad ingresada es {edadUsuario}, estas dentro del rango de los 30\'0 años")
# else:
#     print("No estás dentro del rango")

# # Clase 4, Ejercicio 7
# # El mayor de dos numeros
# # Solicitar al usuario dos valores, numero1 (int) numero2 (int)
# # Se debe imprimir el mayor de los dos numeros, la salida debe ser identica a la siguiente:
# # Digite el valor para el numero1:
# # Digite el valor para el numero2:
# # El numero mayor es: <numeroMayor>
#
# numero1 = int(input("Digite el valor para el numero1: "))
# numero2 = int(input("Digite el valor para el numero2: "))
# if numero1 > numero2:
#     print(f"El número mayor es: {numero1}")
# elif numero2 > numero1:
#     print(f"El número mayor es: {numero2}")
# else:
#     print("Los números deben ser distintos!")

# Clase 4, Ejercicio 8
# Tienda de libros

print("Ingrese los siguientes datos del libro")
nombreLibro = input("Digite el nombre del libro: ")
idLibro = int(input("Digite el ID del libro: "))
precioLibro = float(input("Digite el precio del libro: "))
envioGratis = input("Indicar si el envio es gratuito (True/False): ")
if envioGratis == "True":
    envioGratis = True
elif envioGratis == "False":
    envioGratis = False
else:
    envioGratis = "El valor es incorrecto, debe escribir True/False"

print(f'''
        Nombre: {nombreLibro}
        Id: {idLibro}
        Precio: ${precioLibro}
        Envio gratuito?: {envioGratis}
''')
