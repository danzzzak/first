L = []
def q(L):
    for i in range(len(L)):
        print(int(L) % 10)
        L = int(L) // 10
z = input('4islo?')
z = q(str(int(z)))