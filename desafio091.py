from random import randint
from time import sleep
jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores:')
c = 0
for item in sorted(jogadores, key=jogadores.get, reverse=True):
    c += 1
    print(f'{c}º lugar: {item} com', jogadores[item])
    sleep(.5)
