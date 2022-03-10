from random import randint
from time import sleep
palpite = []
conjunto = []
print('_'*40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-'*40)
quantidade = int(input('Quantidade de jogos você pretende jogar: '))
print('{:-^40}'.format(f'SORTEANDO {quantidade} JOGOS'))
sleep(1)
print()
for c in range(quantidade):
    for p in range(0, 6):
        n = randint(1, 60)
        if n in palpite:
            n = randint(1, 60)
        palpite.append(n)
    conjunto.append(palpite[:])
    palpite.clear()
    conjunto[c].sort()
    print(f'Jogo {c+1}: {conjunto[c]}')
    sleep(0.8)
print('{:-^40}'.format('< BOA SORTE! >'))