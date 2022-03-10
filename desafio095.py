jogadores = []
while True:
    jogador = {'Nome': str(input('Nome: ')).capitalize().strip()}
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    aproveitamento = []
    total = 0
    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        aproveitamento.append(gols)
        total += gols
    jogador['Gols'] = aproveitamento
    jogador['Total'] = total
    jogadores.append(jogador.copy())
    jogador.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        print('-='*30)
        break
    print('-' * 30)
print('Cód.   Nome {:>15}{:>13}'.format('Total', 'Gols'))
print('-'*50)
for f, c in enumerate(jogadores):
    print(' {:<6}'.format(f), end='')
    print('{:<16}{:<13}{}'.format(jogadores[f]["Nome"], jogadores[f]["Total"], jogadores[f]["Gols"]))
while True:
    print('-'*50)
    opci = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opci <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opci]["Nome"]}:')
        for k, c in enumerate(jogadores[opci]["Gols"]):
            print(f'   No jogo {k+1} fez {c} gols.')
    elif opci >= len(jogadores) and opci != 999:
        print(f'ERRO! Não existe jogador com o código {opci}! Tente novamente.')
    if opci == 999:
        break
print('<<< VOLTE SEMPRE >>>')
