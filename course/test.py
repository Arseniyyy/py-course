import math

# Ввод длин сторон треугольника
side1 = float(input("Введите длину первой стороны треугольника: "))
side2 = float(input("Введите длину второй стороны треугольника: "))
side3 = float(input("Введите длину третьей стороны треугольника: "))

# Вычисление полупериметра треугольника
semiperimeter = (side1 + side2 + side3) / 2

# Вычисление площади треугольника по формуле Герона
area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))

# Округление площади до двух знаков после запятой
rounded_area = int(area)

# Вывод результата
print("Площадь треугольника:", rounded_area)

