sum = 0
kolichestvo = 0
q = (input('Введите через проьбел, непустую последовательность целых чисел, оканчивающаяся нулем'))
spisok = q.split()
spisok = [int(i) for i in spisok]
for i in range(len(spisok)):
    sum += spisok[i]
    kolichestvo += 1
print(spisok)
print('Сумма всех = ',sum)
print('Колличество чисел = ', kolichestvo)