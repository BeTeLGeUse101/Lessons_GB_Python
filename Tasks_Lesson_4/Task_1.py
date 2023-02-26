""" Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """

import math

def compute_pi(d):
    s = 0
    n = 0
    while True:
        term = (-1)**n / (2*n + 1)
        s += term
        pi_approx = 4 * s
        if abs(pi_approx - math.pi) < d:
            return pi_approx
        n += 1

d = float(input("Введите дробное число: "))
print(compute_pi(d))