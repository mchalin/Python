import math
from decimal import Decimal


# Manejo de valores infinitos
infinito_positivo = float('inf')
infinito_negativo = float('-inf')
print(f'El valor de infinito_positivo es: {infinito_positivo}')
print(f'Es infinito el positivo? {math.isinf(infinito_positivo)}')
print(f'El valor de infinito_negativo es: {infinito_negativo}')
print(f'Es infinito el negativo? {math.isinf(infinito_negativo)}')

# Modulo math
infinito_positivo = math.inf
infinito_negativo = -math.inf
print(f'El valor de infinito_positivo es: {infinito_positivo}')
print(f'Es infinito el positivo? {math.isinf(infinito_positivo)}')
print(f'El valor de infinito_negativo es: {infinito_negativo}')
print(f'Es infinito el negativo? {math.isinf(infinito_negativo)}')

# Con el módulo decimal
infinito_positivo = Decimal('Infinity')
infinito_negativo = Decimal('-Infinity')
print(f'El valor de infinito_positivo es: {infinito_positivo}')
print(f'Es infinito el positivo? {math.isinf(infinito_positivo)}')
print(f'El valor de infinito_negativo es: {infinito_negativo}')
print(f'Es infinito el negativo? {math.isinf(infinito_negativo)}')
