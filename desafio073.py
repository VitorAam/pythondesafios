times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR',
         'Cruzeiro', 'Botafogo', 'Santos', 'Bahia','Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
         'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print(f'Times organizados em ordem alfabética: {sorted(times)}')
print('='*180)
print(f'No Campeonato Brasileiro de Futebol os 5 primeiros colocados são, em ordem: {times[0:6]}')
print('='*180)
print(f'Os últimos colocados são (em ordem do com mais pontos para o com menos): {times[-4:]}')
print('='*180)
print('O time da Chapecoense está na posição de número {} dentro da tabela.'.format(times.index('Chapecoense')+1))
