""" Даны две записи многочлена. Задача - найти сумму многочленов. """

def sum_polynomials(poly1, poly2):
    result = []
    n = max(len(poly1), len(poly2))
    for i in range(n):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        result.append(coeff1 + coeff2)
    return result

# пример использования функции sum_polynomials
P = [2, 5, -1, 3]
Q = [4, 2, 1]
result = sum_polynomials(P, Q)
print(result)  # [6, 7, 0, 3]