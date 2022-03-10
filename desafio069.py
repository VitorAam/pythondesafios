from datetime import date
h = m = ma = 0
while True:
    print('_' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    a = int(input('Ano de nascimento: '))
    i = date.today().year - a
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-'*20)
    p = str(input('Você quer continuar cadastrando? [S/N] ')).upper().strip()[0]
    if i > 18:
        ma += 1
    if s == 'M':
        h += 1
    elif s == 'F':
        if i < 20:
            m += 1
    if p == 'N':
        break
    while p not in 'SN':
        print('OPÇÃO INVÁLIDA')
        p = str(input('Você quer continuar cadastrando? [S/N] ')).upper().strip()[0]
print('-'*20)
print(f'''No total foram cadastrados {ma} maiores de idade.
{h} homens.
{m} mulheres com menos de 20 anos''')
