""" Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N. 
Пример:
n = 17->[17
n = 3628800 -> [2,3,5,7]"""

def prime_factors(n):

    factors = []

    i = 2 #Начинаем перебор делителей с числа 2.

    while i * i <= n:

        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
        
    return factors

n = int(input("Введите натуральное число: "))
print(prime_factors(n))
