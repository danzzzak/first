x = 1
max = 0
q=input('элементы массива через пробел ')
masiv = q.split()
masiv.pop(0)
masiv = [int(i) for i in masiv]
for i in range(len(masiv)):
    if masiv[i] > 0:
            if max < masiv[i]:
                x=1
                max = masiv[i]
            if masiv[i] == max:
                x *= masiv[i]
print('Произведение положительных максимальных елементов после первого = ', x)
