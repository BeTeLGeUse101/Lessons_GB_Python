# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Введите координату точки Х1: "))
y1 = float(input("Введите координату точки Y1: "))
x2 = float(input("Введите координату точки Х2: "))
y2 = float(input("Введите координату точки Y2: "))

result = ((x2 - x1)**2 + (y2 - y1)**2) ** (0.5)

print(round(result, 2))