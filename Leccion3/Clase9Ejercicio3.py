# Leer 10 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
contPos, contNeg, contNeu = 0, 0, 0
for i in range(10):
    nro = int(input("Ingrese un número: "))
    print()
    print(f"Restan {9-i}")
    if nro == 0:
        contNeu += 1
    elif nro > 0:
        contPos += 1
    else:
        contNeg += 1

print(f'''
    La cantidad de nros positivos:  {contPos}
    La cantidad de nros negativos:  {contNeg}
    La cantidad de nros neutros:    {contNeu}
''')