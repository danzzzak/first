import math

sum = 0
z = 0
def q(n, z, sum):
    n = int(n)
    for i in range(n):
        z = 2 / (math.sqrt(math.factorial(n) + 4))
        sum += z
    print('Сумма ',n,' елементов = ',sum)
n = float(input('Сколько елементов?'))
n = q(n, z, sum)

# ЭТО СУММА ЕЛЕМЕНТОВ А НЕ НОМЕР тоесть это ""Б""
