# COLECCIONES EN PYTHON


# LISTAS []
# (Mutable)

# lista = Juani, Lucia, Maxi

nombres = ["Juani", "Lucia", "Maxi"]
print(nombres)
print(nombres[0:2])  # Solo muestra el índice 0 y 1, pero no el 2

# Ir del inicio de la lista al indice (Sin incluirlo)
print(nombres[:2])  # Indices a mostrar 0, 1

# Ir desde el índice indicado hasta el final
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

# Agregamos varios elementos al final (en la cola)
nombres.append("Vale")
nombres.append([1, 2, 3])  # También puede agregarse otra lista
nombres.append(True)  # Un booleano
nombres.append(12.34)  # Un tipo float
nombres.append([4, 5])  # Otra lista
nombres.append(15)  # Un entero
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, "Coquito")
print(nombres)

nombres.insert(3, "Homero")
print(nombres)

# Eliminamos un elemento
nombres.remove("Homero")
print(nombres)

# Eliminar el último elemento de la lista
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
    "IDE": "Integrated Development Environment",
    "POO": "Programacion Orientada a Objetos",
    "SABD": "Sistema de Administracion de Base de Datos"
}
print(diccionario)

# Cantidad de elementos
print(len(diccionario))

# Acceder a un elemento del diccionario con key
print(diccionario['POO'])

# Otra forma de acceder a los datos
print(diccionario.get('IDE'))

# Modificar elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

# Recorrer los elementos
for termino in diccionario:  # Mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():  # Mostrando llaves y valores con la funcion items
    print(termino, "-", valor)

for termino in diccionario.keys():  # Mostrando solo las llaves
    print(termino)

for valor in diccionario.values():  # Mostrando solo los valores
    print(valor)

# Comprobar si existe un elemento
print('POO' in diccionario)
print('PAA' not in diccionario)  # O no :)

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('IDE')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# Concatenar listas
lista1 = [1, 2, 3, 3]
lista2 = [4, 5, 6, 3]
lista3 = lista1 + lista2
print(lista3)

# Agregar varios elementos a la lista
lista3.extend([7, 8, 9, 3])
print(lista3)

# Mostrar la posicion de un elemento
print(lista3.index(5))
# print(lista3.index(0)) # Sino esta en la lista genera un error

# Cuenta valores repetidos dentro de la lista
print(lista3.count(3))

# Poner una lista al reves
lista3.reverse()
print(lista3)

# Multiplicar una lista repitiendo sus elementos
lista3 *= 3
print(lista3)

# Metodos de ordenamiento, en Python es una funcion
lista3.sort()  # Ordena de forma ascendente
print(lista3)
lista3.sort(reverse=True)  # Ordena de forma descendente
print(lista3)

# Repaso de Tuplas
# No puede modificarse
tupla = (4, 'hola', 7.89, [1, 2, 3], 4, 'Chau')  # Puede tener diferentes tipos de datos dentro
print(tupla)
# Se puede usar index, count, len
# Las tuplas se pueden convertir en listas, y viceversa
print(4 in tupla)  # Consulta booleana, devuelve booleano

# Repaso de set o conjunto
# No puede tener valores repetidos
conjunto2 = set()  # La unica forma de crear un conjunto vacio es con la funcion set()
print(type(conjunto2))

conjunto1 = {}  # Es un diccionario si estan vacias las llaves,
print(type(conjunto1))
conjunto1 = {1}  # Para q lo tome tipo set se debe poner un elemento
print(type(conjunto1))

conjunto2.add(7)
conjunto2.add('hola')
conjunto1.add('Hola')
conjunto1.add(7)

print(conjunto1)
print(conjunto2)

print(3 not in conjunto1)  # Consulta booleana, sino esta en conjunto1, devuelve booleano

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # Se utiliza | para unir dos conjuntos
print(conjunto3)  # No agrega elementos repetidos

conjunto3 = conjunto1 & conjunto2  # Se utiliza & para unir dos conjuntos
print(conjunto3)  # No agrega elementos q no esten repetidos

conjunto3 = conjunto2 - conjunto1  # Asigna el valor que esta en el conjunto 2 y no en el 1
print(conjunto3)
conjunto3 = conjunto1 - conjunto2  # Asigna el valor que esta en el conjunto 1 y no en el 2
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # Elementos que no comparten o son diferentes entre ambos
print(conjunto3)

# Subconjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3))  # para saber si el conjunto1 es subconjunto del conjunto3
print(conjunto2.issubset(conjunto3))  # para saber si el conjunto2 es subconjunto del conjunto3
print(conjunto3.issubset(conjunto1))  # Falso!
print(conjunto3.issubset(conjunto2))  # Falso!

# Superconjunto
print(conjunto3.issuperset(conjunto1))  # Conjunto 3 es un superconjunto de conjunto1
print(conjunto3.issuperset(conjunto2))  # tambien de conjunto2
print(conjunto1.issuperset(conjunto3))  # pero conjunto1 no es superconjunto de conjunto3
print(conjunto2.issuperset(conjunto3))  # y tampoco conjunto2

# Como saber si los conjuntos son disconexos, o sea, sino tienen elementos en comun
print(conjunto1.isdisjoint(conjunto2))

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hace q el conjunto sea totalemten inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso diccionarios
diccionarioNuevo = {
    'Azul': 'Blue',
    'Rojo': 'Red',
    'Verde': 'Green',
    'Amarillo': 'Yellow'
}
print(diccionarioNuevo)

# Eliminar elementos
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {
    'Maxi': {
        'Edad': 39,
        'Altura': 1.76
    },
    'Juan': [29, 1.75],
    'Valeria': [37, 1.69]
}
print(diccionario2['Maxi'])

# Tarea seleccion argentina
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi',
         'Edad': 35,
         'Altura': 1.70,
         'Precio': '50 millones',
         'Posicion': 'Extremo derecho'
         },
    11: {'Nombre': 'Angel Di Maria',
         'Edad': 34,
         'Altura': 1.80,
         'Precio': '12 millones',
         'Posicion': 'Extremo derecho'
         },
    24: {'Nombre': 'Paulo Dybala',
         'Edad': 28,
         'Altura': 1.77,
         'Precio': '35 millones',
         'Posicion': 'Media punta'
         },
    19: {'Nombre': 'Nicolas Otamendi',
         'Edad': 34,
         'Altura': 1.83,
         'Precio': '3.5 millones',
         'Posicion': 'Defensa central'
         },
    23: {'Nombre': 'Emiliano Martinez',
         'Edad': 30,
         'Altura': 1.90,
         'Precio': '28 millones',
         'Posicion': 'Portero'
         },
    1: {'Nombre': 'Franco Armani',
        'Edad': 36,
        'Altura': 1.92,
        'Precio': '3.5 millones',
        'Posicion': 'Portero'
        }
}
print(seleccionArgentina)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print(f'Tenemos cargados en el diccionario la cantidad de: {len(seleccionArgentina)} jugadores')

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacar elementos por el final
elementoBorrado = pila.pop()  # Elimina el ultimo elemento y lo guarda en la variable
print(f'''
Sacamos el elemento: {elementoBorrado}
La pila ahora quedó asi: {pila}
''')

# Colas con lista (estructura tipo FIFO) First in, first out
cola = ['Max', 'Juan', 'Marcelo']

# Agregamos elementos al final de la cola
cola.append('Vale')
cola.append('Lucia')
print(cola)

# Retiramos elementos de la cola
atendido = cola.pop(0)
print(f'Atendido {atendido}')
print(cola)
atendido = cola.pop(0)
print(f'Atendido {atendido}')
print(cola)
atendido = cola.pop(0)
print(f'Atendido {atendido}')
print(cola)
atendido = cola.pop(0)
print(f'Atendido {atendido}')
print(cola)
atendido = cola.pop(0)
print(f'Atendido {atendido}')
print(cola)
