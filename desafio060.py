n = int(input('Digite um número inteiro para descobrir seu fatorial: '))
f = n
r = n
print('{}! é igual a:'.format(n), end=' ')
while f != 1:
    print('{}'.format(f), end=' x ')
    f -= 1
    r *= f
print('1', end=' = ')
print('{}'.format(r))
