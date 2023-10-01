# Tipo bool contiene valores true o false
# En sistema numérico, es false cuando es 0, true para los demás valores

valor = 0
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = -1
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = 5
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = 0.0
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sistema tipo string, es false cuando es '', true para los demás valores

valor = ''
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = ' '
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sistema tipo list o colecciones, es false cuando es [], true para los demás valores
valor = []
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = [1, 2, 3]
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sistema tipo tuple, es false cuando es (), true para los demás valores
valor = ()
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = (1, 2, 3)
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sistema tipo dict, es false cuando es {}, true para los demás valores
valor = {}
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = {'a': 1, 'b': 2}
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sistema tipo set, es false cuando es set(), true para los demás valores
valor = set()
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

valor = {1, 2, 3}
resultado = bool(valor)
print(f'El valor de valor es: {valor}')
print(f'El valor de resultado es: {resultado}')

# En sentencia de control, es false cuando es None, true para los demás valores
if bool(''):
    print('Es true')
else:
    print('Es false')

if bool(' '):
    print('Es true')
else:
    print('Es false')

# Con ciclo while, es false cuando es 0, true para los demás valores
variable = 0
while variable:
    print(variable)
    print('Es true')
    break
else:
    print('Es false')

variable = 1
while variable:
    print(variable)
    print('Es true')
    break
else:
    print('Es false')