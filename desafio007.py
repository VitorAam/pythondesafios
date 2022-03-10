n1 = float(input('Sua nota na primeira unidade foi? '))
n2 = float(input('Sua nota na segunda unidade foi? '))
m = (n1+n2)/2
print('Sua \033[4;36mmédia\033[m nesta matéria é \033[4;36m{:.2f}\033[m'.format(m))
