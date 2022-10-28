# Ejercicio 8: Menu interactivo (cajero automatico)
# Hacer un programa que simule un cajero automatico, con un saldo inicial de $ 1000.
# Tendra el siguiente menú de opciones:
#           1 - Ingresar dinero en la cuenta
#           2 - Retirar dinero de la cuenta
#           3 - Mostrar dinero disponible
#           4 - Salir

saldo = 1000
while True:
    print(f'''
1 - Ingresar dinero de la cuenta
2 - Retirar dinero de la cuenta
3 - Mostrar dinero disponible
4 - Salir''')
    entrada = int(input("Ingrese una opcion del menu: "))
    if entrada == 1:
        saldo += float(input("Cantidad de dinero a ingresar: $"))
        print(f'El saldo en la cuenta es de: ${saldo}')
    elif entrada == 2:
        retirar = float(input("Ingrese cantidad a retirar: $"))
        if retirar > saldo:
            print(f"No alcanza a retirar ${retirar}, Ud tiene en su cuenta: ${saldo}")
        else:
            saldo -= retirar
            print(f'El saldo en la cuenta es de: ${saldo}')
    elif entrada == 3:
        print(f'El saldo es: ${saldo}')
    elif entrada == 4:
        break
    else:
        print('Ingrese una opción valida.')

