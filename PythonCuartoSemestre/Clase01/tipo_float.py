# Profundizando en el tipo float

a = 3.0
print(f'El valor de a es: {a}')
print(f'El valor de a es: {a:.2f}')
print(f'El tipo de dato de a es: {type(a)}')

# Constructor float()
# Puede recibir como argumento un valor entero o un valor string

# Le pasamos un valor entero
b = float(3)
print(f'El valor de b es: {b}')
print(f'El valor de b es: {b:.2f}')
print(f'El tipo de dato de b es: {type(b)}')

# Le pasamos un valor string
c = float('3.0')
print(f'El valor de c es: {c}')
print(f'El valor de c es: {c:.2f}')
print(f'El tipo de dato de c es: {type(c)}')

# Notación exponencial (valores positivos o negativos)
d = 3e5
print(f'El valor de d es: {d}')
print(f'El valor de d es: {d:.2f}')
print(f'El tipo de dato de d es: {type(d)}')

e = 3e-5
print(f'El valor de e es: {e}')
print(f'El valor de e es: {e:.5f}')
print(f'El tipo de dato de e es: {type(e)}')

# Cualquier calculo que incluye un float devuelve un float
f = 3.0 + 2
print(f'El valor de f es: {f}')
print(f'El valor de f es: {f:.2f}')
print(f'El tipo de dato de f es: {type(f)}')

