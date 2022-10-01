# Dadas las horas trabajadas de 5 personas y la tarifa de pago,
# calcular el salario y la sumatoria de todos los salarios
suma = 0
for i in range(5):
    print(f"Salario del empleado No {i+1}:")
    horas = int(input("   Ingrese las horas trabajadas: "))
    tarifa = float(input("   Ingrese la tarifa por hora ($): "))
    salario = tarifa * horas
    print(f"   El salario es: ${salario}")
    print()
    suma += salario

print(f"La suma de todos los salarios es: ${suma}")