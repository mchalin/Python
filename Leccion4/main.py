# LISTAS []
# (Mutable)

# lista = Juani, Lucia, Maxi

nombres = ["Juani", "Lucia", "Maxi"]
print(nombres)
print(nombres[0:2])  # Solo muestra el indice 0 y 1, pero no el 2

# Ir del inicio de la lista al indice (Sin incluirlo)
print(nombres[:2])  # Indices a mostrar 0, 1

# Ir desde el indice indicado hasta el final
print(nombres[1:])  # Indices a mostrar 1,2

# Imprimimos por indice
print(nombres[0])
print(nombres[1])
print(nombres[2])

# El último
print(nombres[-1])

# Modificamos un valor
nombres[2] = "mAZi"
nombres[1] = "Chula"
print(nombres)

# Revisar si un elemento existe dentro de la lista
print("Maxi" in nombres)
# Sino existe..
print("Alberto" not in nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)
else:
    print("Se acabaron los elementos")

# Mostramos la cantidad de elementos
print(len(nombres))

# Agregamos un elemento al final (en la cola)
nombres.append("Vale")
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Coquito")
print(nombres)

nombres.insert(3, "Homero")
print(nombres)

# Eliminamos un elemento
nombres.remove("Homero")
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[1]
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)

# TUPLAS ()
# (No mutables, no se pueden modificar)

# Definimos una tupla
cocina = ("Cuchara", "Cuchillo", "Tenedor")
print(cocina)

# Cantidad de elementos
print(len(cocina))

# Acceder a un elemento - Se usan corchetes, no parentesis, funciona al igual q las listas
print(cocina[1])
print(cocina[:2])
print(cocina[-1])

# Revisar si un elemento existe dentro de la tupla
print("Cuchillo" in cocina)
# Revisamos sino existe
print("Cucharita" not in cocina)

# Ejemplo
verduras = ("papa",)  # Para declarar una tupla es necesario que aunq sea solo un elemento, se le proporcione una coma
print(verduras)

# Recorrer la tupla
for elemento in cocina:
    print(elemento, end=" ")  # Cambiamos el salto de linea en print, para que se vea en una sola linea
else:
    print("\nSe terminó de imprimir la tupla")

# CONJUNTOS set o {}
# (No tiene un orden ni indice, no se pueden almacenar datos repetidos)
# (No se puede modificar, si se puede agregar y borrar)

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Cantidad de elementos
print(len(planetas))

# Revisar si un elemento existe dentro del set
print("Marte" in planetas)
# Revisamos sino existe en el set
print("Tierra" not in planetas)

# Agregar un elemento
planetas.add("Tierra")

# Recorrer el set
for dato in planetas:
    print(dato)

# Eliminar elementos, puede arrojar un error si no existe el elemento
planetas.remove("Venus")

# Para evitar que arroje error sino encuentra el elemento, se puede utilizar discard
planetas.discard("Tierras")
print(planetas)

# Limpiar
planetas.clear()
print(planetas)

# Eliminar set
del planetas

# DICCIONARIO
# Un diccionario esta compuesto por dos elementos. No tiene indice, utiliza las llaves.
# Una llave y un valor
# dict(key, value)
diccionario = {
    "IDE":"Integrated Development Environment",
    "POO":"Programacion Orientada a Objetos",
    "SABD":"Sistema de Administracion de Base de Datos"
}
print(diccionario)

# Cantidad de elementos
print(len(diccionario))

# Acceder a un elemento
