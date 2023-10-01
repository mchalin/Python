help(str.join)

tupla_1 = ("hola", "mundo", "!!!")
lista_1 = ["chau", "mundo", "!!!"]
cadena_1 = " ".join(tupla_1)
cadena_2= " ".join(lista_1)
print("tupla 1: ", tupla_1)
print("lista 1: ", lista_1)
print("cadena 1: ", cadena_1)
print("cadena 2: ", cadena_2)

texto_1 = "holamundo!!!"
cadena_3 = ".".join(texto_1)
print("texto 1: ", texto_1)
print("cadena 3: ", cadena_3)


diccionario_1= {"clave1": "valor1", "clave2": "valor2"}
cadena_keys = "-".join(diccionario_1.keys())
cadena_values = "-".join(diccionario_1.values())
print("diccionario 1: ", diccionario_1)
print("Keys: ", cadena_keys)
print("tipo: ", type(cadena_keys))
print("Values: ", cadena_values)
print("tipo: ", type(cadena_values))