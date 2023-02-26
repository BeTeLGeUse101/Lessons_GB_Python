"""Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
Пример: [1,2,3,4,5,2,3,1] -> [1,2,3,4,5]"""

seq = input("Введите последовательность чисел: ")

unique_seq = []

for num in seq:
    # Если элемент еще не встречался, добавляем его в список уникальных элементов
    if num not in unique_seq:
        unique_seq.append(num)

print(unique_seq)
