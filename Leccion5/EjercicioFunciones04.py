# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

# Creamos la función
def calcular_total_pago(pago_sin_impuesto, impuesto):  # Parámetros
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total


# Solicita al usuario se ingresen argumentos para la función
pago_sin_impuesto = float(input("Ingrese el monto del pago sin impuestos ($): "))
impuesto = float(input("Ingrese el impuesto (%): "))

# Ejecutamos la función
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)  # Argumentos
print(f"El pago total con impuesto del %{impuesto} es: ${pago_con_impuesto}")
