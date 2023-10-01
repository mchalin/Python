import math
from _pydecimal import Decimal

# NaN (Not a number)
a = float('NaN')
print(f'El valor de a es: {a}')
print(f'Es NaN? {math.isnan(a)}')
print(f'El tipo de dato de a es: {type(a)}')
b = float('2.2')
print(f'El valor de b es: {b}')
print(f'Es NaN? {math.isnan(b)}')
print(f'El tipo de dato de b es: {type(b)}')
c = Decimal('NaN')
print(f'El valor de c es: {c}')
print(f'Es NaN? {math.isnan(c)}')
print(f'El tipo de dato de c es: {type(c)}')


