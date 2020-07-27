print('Введите значение аргумента')
import math
try:
    x=float (input('Введите х',))
    try:
        y = ((2 * math.log(x) * math.cos(2 * x) - (3 * (((x + 1) ** 2) / (x - 1)))) / (2 + math.sqrt(x)))
        print('y = ',y)
    except ZeroDivisionError:
        print('При значении в еденицу происходит деление на 0')
except ValueError:
    print('Использованы буквы')