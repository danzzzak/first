K = 0
N = int(input('Введите число N = '))
while 2 ** K <= N:
    K += 1
print('Наибольшее целое число K, при котором выполняется неравенство (2^K > N) = ',K)