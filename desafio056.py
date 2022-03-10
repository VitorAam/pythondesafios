m = 0
hv = 0
nvm = ''
sm = 0
for c in range(1, 5):
    print('{:-^21}'.format('{}ª PESSOA'.format(c)))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    m = (m + i)
    if s == 'M' and i > hv:
        hv = i
        nvm = n
    elif s == 'F' and i < 20:
        sm = sm + 1
print('A média de idade do grupo é {}.'.format(m/4))
if nvm != '':
    print('O homem mais velho do grupo é: {}.'.format(nvm))
print('Nesse grupo, existem {} mulheres com menos de 20 anos.'.format(sm))
