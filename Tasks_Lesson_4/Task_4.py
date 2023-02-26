""" Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 """

import random

# Задаем степень многочлена
k = 2

# Генерируем случайные коэффициенты
coefficients = [random.randint(0, 100) for _ in range(k + 1)]

# Формируем многочлен заданной степени
def polynomial(x):
    result = 0
    for i in range(k + 1):
        result += coefficients[i] * (x ** i)
    return result

print(polynomial(2))