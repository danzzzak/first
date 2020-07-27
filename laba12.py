print('Введите значение аргумента')
import math
try:
    try:
        x=float (input('x = ',))
        z1=(math.sin(2*x)+math.sin(5*x)-math.sin(3*x)) / (math.cos(x)-math.cos(3*x)+math.cos(5*x))
        z2= math.tan(3*x)
        print('z2 = ',z2)
        print('z1 = ',z1)
    except ZeroDivisionError:
        print('Происходит деление на 0')
except ValueError:
    print("Использованы буквы")
