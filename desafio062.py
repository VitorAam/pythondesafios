barra = ('='*60)
print(barra)
print('{:^60}'.format('CALCULANDO PROGRESSÃO ARITMÉTICA (P.A.)'))
print(barra)
i = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão aritmética: '))
d = i
count = 1
pergunta = '''
Você quer ver mais termos?

Caso sim, digite quantos termos a mais você quer ver.
Caso não, digite [0]

Número de termos: 
'''
print('Os dez primeiros termos dessa razão são: ')
if count == 1:
    print('{}'.format(i), end=' >')
while count != 10:
    d += + r
    print('{}'.format(d), end='')
    count += 1
    if count != 10:
        print(end=' >')
print(end='\n')
menu = int(input(pergunta))
while menu != 0:
    while count != 10 + menu:
        d += + r
        print(f'{d}', end='')
        print(' >' if count != 9 + menu else '\n', end='')
        count += 1
    if count == 10 + menu:
        print(barra)
        menu = int(input(pergunta))
if menu == 0:
    print('-=-'*15)
    print('FIM DO PROGRAMA')