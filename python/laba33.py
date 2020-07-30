import math
print("Введите коэффициенты для квадратного уравнения (ax^2 - (3-c)x - c = 0):")
a = float(input("a = "))
c = float(input("c = "))
b=-(3-c)
D = b ** 2 - 4 * a * c
print("D = %.2f" % D)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    if x1>x2:
        print(x1)
    else:
        print(x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")