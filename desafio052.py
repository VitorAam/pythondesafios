numero = int(input('Digite um número: '))
n = []
for c in range(1, numero +1):
    nn = numero % c
    n.append(nn)
rr = n.count(0)
if rr == 2:
    print('Sem duvidas {} é um número primo!'.format(numero))
else:
    print('O número {} não é um número primo.'.format(numero))

