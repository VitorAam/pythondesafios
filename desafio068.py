from random import randint
print('-=-'*7)
print('JOGO DO PAR OU ÍMPAR')
print('-=-'*7)
c = 0
while True:
    n = int(input('Digite um valor: '))
    j = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print('-=-' * 7)
    pc = randint(0, 10)
    s = pc + n
    if s % 2 == 0:
        print(f'O PC jogou {pc} e você {n}, resultando em {s}, que é PAR!')
        print('-=-' * 7)
        if j == 'P':
            print('Você GANHOU.')
            print('Vamos jogar de novo...')
        else:
            print('Você PERDEU.')
            break
    else:
        print(f'O PC jogou {pc} e você {n}, resultando em {s}, que é ÍMPAR!')
        print('-=-' * 7)
        if j == 'I':
            print('Você GANHOU.')
            print('Vamos jogar de novo...')
        else:
            print('Você PERDEU.')
            break
    c += 1
print('GAME OVER!!!')
print('-=-'*7)
print(f'Você alcançou {c} vitórias consecutivas!')
