import random
Max = 0
m = int(input('Сколько строк?'))
L = [random.randint(1,2) for i in range(m)] #Что бы создать елементы i а потом их заменить
print('Введите',m,'строк')
for i in range(m):
    L[i] = input('Введите строку - ')
print(L)
for i in range(m):
    if len(L[i]) > Max:
        Max = len(L[i])
print('max = ', Max)
for i in range(m):
    Rovn9em = Max - len(L[i])
    print('*' * Rovn9em + str(L[i]))