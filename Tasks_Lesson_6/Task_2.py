""" Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума) """

import random

my_list = []

for i in range(10):
    my_list.append(random.randint(-10, 10))

print(my_list)

min_value = int(input("Введите минимальный диапазон: "))
max_value = int(input("Введите максимальный диапазон: "))

for i in range(len(my_list)):
    if min_value <= my_list[i] <= max_value:
        print(i)