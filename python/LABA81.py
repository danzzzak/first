import math

z = 0
def q(n, z):
    n = int(n)
    for i in range(n):
        z = 2 / (math.sqrt(math.factorial(n) + 4))
    print(n, '-ый елемент = ', z)
n = float(input('Nomer etementa?'))
n = q(n, z)

#проверенно на калькуляторе

