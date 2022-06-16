# Escribí un programa para solicitar al usuario tres números 
# y mostrar en pantalla al menor de los tres.
 
# Ejemplo de ejecución:

# Primer número: 20
# Segundo número: 30
# Tercer número: 10
# Menor: 10

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

if num1 < num2 and num1 < num3:
    print(f"El número mas pequeño es {num1}")
elif num2 < num1 and num2 < num3:
    print(f"El número mas pequeño es {num2}")
elif num3 < num1 and num3 < num2:
    print(f"El número mas pequeño es {num3}")
else:
    print("No debe ingresar dos números iguales!!")
