import math

n = 0
x = -7
dx = 1
print('Таблица значений функции')
print('--------------------')
print('|  n  |  x  |   y  |')
print('--------------------')

while n < 18:
    for i in range(18):
        x += dx
        n += 1
        if x <= -3:
            y = 3
        if -3 < x <= 3 :
            y = 3 - math.sqrt(9 - x ** 2)
        if 3 < x <= 6 :
            y = -2 * x + 9
        if x > 6 :
            y = x - 9
        print('|', '%-3s'%n, '|', '%-3s'%x, '|', '%.2f' % y, '|')



