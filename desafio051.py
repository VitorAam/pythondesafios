print('='*60)
print('{:^60}'.format('CALCULANDO PROGRESSÃO ARITMÉTICA (P.A.)'))
print('='*60)
i = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão aritmética: '))
d = i + (10 - 1) * r
print('Os dez primeiros termos dessa razão são: ')
for c in range(i, d + r, r):
    print(c, end='> ')
print('FIM')
