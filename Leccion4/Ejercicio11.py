# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos.
# Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono.
# El programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir
print("Agenda telefónica.")
agenda = {}
while True:
    print(f'''
    1. Nuevo contacto
    2. Borrar contacto
    3. Ver contactos existentes
    4. Salir
''')
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        nuevocontacto = input("Ingrese nombre del nuevo contacto: ")
        nuevocontactotel = int(input("Ingrese teléfono del nuevo contacto: "))
        if nuevocontacto not in agenda:
            agenda[nuevocontacto] = nuevocontactotel
            print("Se agregó el contacto.")
        else:
            print("El contacto ya existe!")
    elif opcion == 2:
        borrarcontacto = input("Ingrese nombre del contacto a borrar: ")
        if borrarcontacto in agenda:
            del (agenda[borrarcontacto])
            print(f"Se borró el contacto {borrarcontacto}.")
        else:
            print("No existe ese nombre en la agenda.")
    elif opcion == 3:
        print("Mostrando agenda:")
        for nombre, telefono in agenda.items():
            print(f'Nombre: {nombre} @ Teléfono: {telefono}')
    elif opcion == 4:
        print("Gracias por utilizar la agenda en Python")
        break
    else:
        print(f"Opción seleccionada ({opcion}) no válida.")
