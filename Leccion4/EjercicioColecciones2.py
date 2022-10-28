# Ejercicio 2: Operaciones de conjuntos de listas
# Escriba un programa q tenga dos listas y que a continuacion
# cree las siguientes listas (en las que no debe haber repeticion)
# 1 - Lista de palabras que aparecen en las listas
# 2 - Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 - Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 - Lista de palabras que aparecen en ambas listas

lista1 = ["Hola", "Chau", 1, 2, 3, 7, 8, 9, 3]
lista2 = ["Hola", "Que", "Tal", 2, 4, 6, 8, 10, 4]
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

lista3 = list(set(lista1) | set(lista2))
print(f"\n1 - Lista de palabras que aparecen en las listas \n{lista3} [Tipo de lista3: {type(lista3)}]")

lista3 = list(set(lista1) - set(lista2))
print(f"\n2 - Lista de palabras que aparecen en la lista 1 pero no en la lista 2 \n{lista3} [Tipo de lista3: {type(lista3)}]")

lista3 = list(set(lista2) - set(lista1))
print(f"\n3 - Lista de palabras que aparecen en la lista 2 pero no en la lista 1 \n{lista3} [Tipo de lista3: {type(lista3)}]")

lista3 = list(set(lista2) & set(lista1))
print(f"\n4 - Lista de palabras que aparecen en ambas listas \n{lista3} [Tipo de lista3: {type(lista3)}]")


