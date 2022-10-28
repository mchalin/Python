# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista sin repetir caracteres
print("Programa para no repetir caracteres.")
cadena = input("Ingrese una cadena de texto: ")
lista = []

# # Caso 1
# for letra in cadena:
#     lista.append(letra)
# lista = list(set(lista))
# print(lista)

# Caso 2
for letra in cadena:
    if letra not in lista:
        lista.append(letra)
print(f'Lista sin repetir caracteres: {lista}')