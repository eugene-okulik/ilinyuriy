# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
# Подразумевается, что пользователь сам введет значения a и b с типом int или float

import math

a = input()
b = input()
print((a + b) / 2)  # среднее арифметическое
print(math.sqrt(a * b))  # среднее геометрическое
