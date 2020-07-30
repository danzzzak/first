import math

t = float(input('to4nost='))
n=1
s = 2/(math.sqrt(math.factorial(1)+4))
x=1
while s > t:
    z=2/(math.sqrt(math.factorial(n)+4))
    n += 1
    s += z
    x += 1
print(s)
print(n)