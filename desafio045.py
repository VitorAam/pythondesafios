from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc1 = randint(0, 2)
pc = itens[pc1]
print('\033[33m-=-\033[m'*15)
print('\033[35mJOGO DE JOKENPÔ\033[m')
print('\033[33m-=-\033[m'*15)
sleep(1)
j1 = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!!')
sleep(0.6)
print('-=-'*11)
print('''Você jogou {}
O computador jogou {}'''.format(itens[j1], itens[pc1]))
print('-=-'*11)
if pc1 == 0:
    if j1 == 0:
        print('Deu empate!')
    elif j1 == 1:
        print('Parabéns, você venceu!')
    elif j1 == 2:
        print('O computador venceu. :/')
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente')
elif pc1 == 1:
    if j1 == 0:
        print('O computador venceu. :/')
    elif j1 == 1:
        print('Deu empate!')
    elif j1 == 2:
        print('Parabéns, você venceu!')
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente')
elif pc1 == 2:
    if j1 == 0:
        print('Parabéns, você venceu!')
    elif j1 == 1:
        print('O computador venceu. :/')
    elif j1 == 2:
        print('Deu empate!')
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente')
