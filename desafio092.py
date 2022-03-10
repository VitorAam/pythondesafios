from datetime import datetime
dados = {'Nome': str(input('Nome: '))}
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    concluido = datetime.now().year - dados['Contratação']
    dados['Aposentadoria'] = dados['Idade'] + (35 - concluido)
for k, c in dados.items():
    print(f'{k} tem o valor {c}')
