# Profundizando en el tipo string
import math

# Concatenación de strings automática
a = 'Hola'
b = 'Mundo'
c = a + b
c += '!'

print(f'El valor de c es: {c}')
print(f'El tipo de dato de c es: {type(c)}')

# Concatenación de strings manual
d = 'Hola' 'Mundo'
print(f'El valor de d es: {d}')
print(f'El tipo de dato de d es: {type(d)}')

# Multiplicación de strings
e = 'Hola' * 3
print(f'El valor de e es: {e}')
print(f'El tipo de dato de e es: {type(e)}')

# Constructor str()
# Puede recibir como argumento un valor entero, un valor float o un valor string

# Le pasamos un valor entero
f = str(3)
print(f'El valor de f es: {f}')
print(f'El tipo de dato de f es: {type(f)}')

# Le pasamos un valor float
g = str(3.0)
print(f'El valor de g es: {g}')
print(f'El tipo de dato de g es: {type(g)}')

# Le pasamos un valor string
h = str('3.0')
print(f'El valor de h es: {h}')
print(f'El tipo de dato de h es: {type(h)}')

# Constructor str() con valores booleanos
i = str(True)
print(f'El valor de i es: {i}')
print(f'El tipo de dato de i es: {type(i)}')

j = str(False)
print(f'El valor de j es: {j}')
print(f'El tipo de dato de j es: {type(j)}')

# Constructor str() con valores None
k = str(None)
print(f'El valor de k es: {k}')
print(f'El tipo de dato de k es: {type(k)}')

# Constructor str() con valores nan
l = str(float('nan'))
print(f'El valor de l es: {l}')
print(f'El tipo de dato de l es: {type(l)}')

# Usamos la clase help() para ver la documentación
help(str)
help(math.isnan)

