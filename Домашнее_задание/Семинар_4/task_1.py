# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math
from decimal import Decimal

d = Decimal(input('Введите точность: '))

print(round(math.pi, int(math.log(d, 0.1))))