n = 129
l = [i for i in range(n)]
l.pop(0)
print(l)
z=0
for i in range(int(len(l))):
    i += 1
    z = 1 / ((2 * i) ** 2) + z
print('Сумма = ', '%.6f' % z)
print(i)
#Проверено на калькуляторе
