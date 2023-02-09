# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите число Х: "))
y = int(input("Введите число Y: "))
z = int(input("Введите число Z: "))

left = not (x or y or z)
  
right = not x and not y and not z
  
print(left == right)