masiv=input('Элементы через пробел ').split()
print(masiv)
q=0
for i in range(int(len(masiv) / 2)): # Так как цикл обрабатывает сразу 2 числа то нужно в 2 раза меньше циклов
    z=masiv[q]
    masiv[q]=masiv[q+1]
    masiv[q+1]=z
    q += 2
print(masiv)