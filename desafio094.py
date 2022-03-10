pessoas = []
mulheres = []
acima = []
itotal = 0
while True:
    dados = {'Nome': str(input('Nome: ')),
             'Sexo': str(input('Sexo [M/F]: ')).strip()[0],
             'Idade': int(input('Idade: '))}
    itotal += dados['Idade']
    while dados['Sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F na informação a seguir.')
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip()[0]
    pessoas.append(dados.copy())
    resposta = str(input('Quer continuar? [S/N] '))[0]
    dados.clear()
    while resposta not in 'NnSs':
        print('ERRO! Responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] '))[0]
    if resposta in 'Nn':
        break
media = itotal/len(pessoas)
for t, p in enumerate(pessoas):
    if pessoas[t]['Idade'] > media:
        acima.append(pessoas[t])
    if pessoas[t]['Sexo'] in 'Ff':
        mulheres.append(pessoas[t]['Nome'])
print(f''' -- Foram cadastradas {len(pessoas)} pessoas.
 -- A média de idade do grupo é de {media} anos.
 -- As mulheres do grupo são: {mulheres}.
 -- As pessoas acima da idade média são: ''')
for t, p in enumerate(acima):
    print('     ', end='')
    for k, v in p.items():
        print(f'{k} = {v}; ', end='')
    print()
print('<<< ENCERRADO >>>')
