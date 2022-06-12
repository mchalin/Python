"""# Ciclo While (Mientras o durante)

contador = 0
while contador < 20:
    print(f"Ejecutamos nuestro ciclo while { contador}")
    contador += 1
else:
    print("El ciclo while ha terminado")

maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
print()

minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
    """
# Ciclo For (Para)
cadena = "Hola"
for letra in cadena:
    print(letra)
else:
    print("El ciclo for ha terminado")
print()

for letra in 'Alemania':
    if letra == 'm':
        print(f"Encontramos la letra: {letra}")
        break
else:
    print("El ciclo for ha terminado")

# Palabra reservada continue
for i in range(10):
    if i % 2 == 0:
        print(f"Valor de i: {i}")

for i in range(10):
    if i % 2 != 0:
        continue
    print(f"Valor de i: {i}")

