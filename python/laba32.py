import math
kat1=float(input('Первый катет?'))
kat2=float(input('Второй катет?'))
gep=math.sqrt(kat1**2+kat2**2)
ygol=math.degrees(math.sin(kat1/gep))
print(gep, ygol)
#math.degrees-из радианы в градусы