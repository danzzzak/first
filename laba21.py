import math


try:
    x=float (input('x = '))
    if x>3:
        y=0.5*x
    if 0 <= x <= 3:
        y = 2
    if x<0:
         y=1/x
    print('y = ',y)
except ValueError:
    print('Использованы буквы')