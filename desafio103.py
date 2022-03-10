def ficha(jogador='d', gols=0):
    v = f'O jogador {jogador} fez {gols} gol(s) no campeonato.'
    return v


# programa principal
r1 = input('Nome do jogador: ').strip()
r2 = input('Número de Gols: ')
if r2.isnumeric():
    r2 = int(r2)
else:
    r2 = 0
print(ficha(r1 if r1 != '' else '<desconhecido>', r2))
