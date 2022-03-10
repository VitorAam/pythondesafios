print('='*60)
print('{:^60}'.format('CALCULANDO PROGRESSÃO ARITMÉTICA (P.A.)'))
print('='*60)
i = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão aritmética: '))
d = i
count = 0
print('Os dez primeiros termos dessa razão são: ')
if count == 0:
    print('{}'.format(i), end=' >')
while count != 9:
    d += + r
    print('{}'.format(d), end='')
    print(' >' if count < 8 else '\n', end='')
    count += 1
print('FIM')
