import math

n = input("Количество измерений пространства: ")
print("Через пробел")
a = input("введите " + n + " координаты 1-ой точки: ")
b = input("введите " + n + " координаты 2-ой точки: ")
c = input("введите " + n + " координаты 3-ой точки: ")
n = int(n)
a = a.split() #разбитие строки на части
b = b.split()
c = c.split()
if len(a) != n or len(b) != n:
    print("Неверный ввод!")
    exit()
S12=S23=S13=0
for i, j in zip(a, b): #zip =апиляция к нескольким объектам(спискам)
    S12 += (int(i) - int(j)) ** 2 #int = число в десятичную систему
for i, j in zip(a, c):
    S13 += (int(i) - int(j)) ** 2
for i, j in zip(b, c):
    S23 += (int(i) - int(j)) ** 2
D12 = math.sqrt(S12)
D13 = math.sqrt(S13)
D23 = math.sqrt(S23)
if D13<D12 and D23<D12:
    Dmax=D12
    m='1 и 2'
if D12<D13:
    if D23<D13:
        Dmax=D13
        m='1 и 3'
if D12<D23 and D13<D23:
    Dmax=D23
    m='2 и 3'
print("Максимальная длина между точками - ", m, "Растояние между ними = ""%.5f"%Dmax)