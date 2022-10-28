# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion
# Elimine los elementos repetidos. Por último mostrar la lista

lista = ["Hola", "Chau", 1, 2, 3, "Hola", "Chau", 3]  # Primer lista con elementos repetidos
print(f"Lista 1 (con elementos repetidos): {lista}")

lista2 = list(set(lista))  # Convertimos a conjunto para eliminar repetidos
print(f"Lista 2 (sin elementos repetidos): {lista2}")
