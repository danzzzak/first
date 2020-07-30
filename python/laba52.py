masiv = input('Введите элементы через пробел ').split()
masiv = [int(i) for i in masiv]
x=0
z=0
pol = 0
for i in range(len(masiv)):
    if x == 0:
        if masiv[i] > 0:
            if masiv[i] == masiv[i-1]:
                try:
                    masiv.pop(i)
                    masiv.pop(i-1)
                    x = 1
                except IndexError:
                    print('Слишком маленькая длинна масива')
                    z = 1
if z == 0 and x == 1:
    print(masiv)
else:
    print('Нет двух подряд идущих положительных чисел')

