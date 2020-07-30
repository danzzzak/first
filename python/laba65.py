#Вводим елемент в строку,добовляем сумму, если елемент нечётный то он = елемент + сумма, добовляем строку в массив

stroka = 5
stolbec = 6
m = []
sum = 0
for i in range(stolbec):
    list = []
    sum = 0
    for j in range(stroka):
        e = float(input('Введите елемент'))
        if e % 2 == 1:
            e += sum
        sum += e
        list.append(e)
    m.append(list)
for g in range(6):
    print(m[g])