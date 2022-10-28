# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

lista = []
# Creamos diccionarios
personaje1 = {
    "Nombre": "Aragon",
    "Clase": "Guerrero",
    "Raza": "Dúnadan del norte"
}
personaje2 = {
    "Nombre": "Gandalf",
    "Clase": "Mago",
    "Raza": "Istar"
}
personaje3 = {
    "Nombre": "Legolas",
    "Clase": "Arquero",
    "Raza": "Elfo Sindar"
}
lista.extend([personaje1, personaje2, personaje3])
# print(lista)
print(f"Lista de personajes lista {type(lista)} con diccionario dentro")
for item in lista:
    print(item)