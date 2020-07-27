import math
x=float (input('х = ',))
if x <= -3:
    y=3
if -3 < x <= 3:
    y = 3 - math.sqrt(9 - x ** 2)
if 3 < x <= 6:
    y= -2 * x + 9
if x>6:
    y= x - 9
print('y = ', y)