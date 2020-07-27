import numpy as np
import random
n = int(input('Размер матрицы = '))
A = np.random.randint(0, 10, (n, n))
A2=np.dot(A,A)
A3=np.dot(A2,A)
print('A = \n',A)
print('A^3 = \n', A3)