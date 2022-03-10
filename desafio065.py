r = 's'
s = ma = me = c = 0
while r == 's':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Você quer continuar? [s/n]: ')).strip().lower()[0]
    s += n
    c += 1
    if n > ma:
        ma = n
    if c == 1:
        me = n
    elif n < me:
        me = n
print('A média de todos os números digitados é: {:.1f}, no total de {} números digitados.'.format(s/c, c))
print('O maior número dentre eles é: {}.'.format(ma))
print('O menor número dentre eles é: {}.'.format(me))
