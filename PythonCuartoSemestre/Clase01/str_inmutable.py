help(str.capitalize)
mensaje1 = "hola mundo"
mensaje2 = mensaje1.capitalize()

print("mensaje1: ", mensaje1)
print("mensaje2: ", mensaje2)
print("mensaje1 es mensaje2: ", mensaje1 is mensaje2)
print("mensaje1 == mensaje2: ", mensaje1 == mensaje2)
print("id(mensaje1): ", id(mensaje1))
print("id(mensaje2): ", id(mensaje2))
print("type(mensaje1): ", type(mensaje1))
print("type(mensaje2): ", type(mensaje2))

mensaje1 += "!!!"
print("mensaje1: ", mensaje1)
print("id(mensaje1): ", id(mensaje1))
print("type(mensaje1): ", type(mensaje1))

mensaje1 = "ajaj"
print("mensaje1: ", mensaje1)
print("id(mensaje1): ", id(mensaje1))
print("type(mensaje1): ", type(mensaje1))

# Al cambiar el valor de mensaje1, se crea un nuevo objeto

mensaje3 = "hola mundo"
mensaje4 = mensaje3
print(f"mensaje3: {mensaje3}", id(mensaje3))
print(f"mensaje4: {mensaje4}", id(mensaje4))
print(f"mensaje3 es mensaje4: {mensaje3 is mensaje4}")
print(f"mensaje3 == mensaje4: {mensaje3 == mensaje4}")
mensaje3 = "hola mundo!!!"
print(f"mensaje3: {mensaje3}", id(mensaje3))
print(f"mensaje4: {mensaje4}", id(mensaje4))
print(f"mensaje3 es mensaje4: {mensaje3 is mensaje4}")
print(f"mensaje3 == mensaje4: {mensaje3 == mensaje4}")
mensaje3 = "hola mundo"
print(f"mensaje3: {mensaje3}", id(mensaje3))
print(f"mensaje4: {mensaje4}", id(mensaje4))
print(f"mensaje3 es mensaje4: {mensaje3 is mensaje4}")
print(f"mensaje3 == mensaje4: {mensaje3 == mensaje4}")


