# Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit
# (debe permitir decimales) y le muestre el equivalente en grados Celsius.
# La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_

temp = float(input("Ingrese la temperatura en escala Fahrenheit: "))
tempCelcius = (5/9) * (temp-32)
print(f"Gracias a este conversor, podemos decir q {temp} Fahrenheit equivalen a {tempCelcius}° Celcius.")