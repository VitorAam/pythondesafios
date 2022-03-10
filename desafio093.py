jogador = {'Nome': str(input('Nome: '))}
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
aproveitamento = []
total = 0
for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c+1}? '))
    aproveitamento.append(gols)
    total += gols
jogador['Gols'] = aproveitamento[:]
jogador['Total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, c in jogador.items():
    print(f'O campo {k} tem o valor {c}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in aproveitamento:
    print('{:>5}Na partida {}, fez {} gols.'.format('=>', c, aproveitamento[c-1]))
print(f'Fez um total de {total} gols.')
