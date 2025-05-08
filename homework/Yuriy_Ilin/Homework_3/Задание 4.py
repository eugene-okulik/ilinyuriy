# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math

katet_a = input()
katet_b = input()

print(f'Гипотенуза: {math.sqrt(katet_a**2 + katet_b**2)}')
print(f'Площадь: {katet_a * katet_b / 2}')
