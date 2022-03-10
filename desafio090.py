aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = str('Aprovado')
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = str('Recuperação')
else:
    aluno['situação'] = str('Reprovado')
for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}')
