n = int(input('Escreva o número de elementos que você quer ver da Sequência de Fibonacci: '))
fib = 0
a = 0
nv = 1
cont = 0
print('Os termos são:\n')
print(fib, end=' ')
while fib+1 != n:
    fib += 1
    cont += 1
    if cont % 2 == 0:
        a += nv
        print(a, end=' ')
    else:
        nv += a
        print(nv, end=' ')
print('\n')
print('FIM DO PROGRAMA')
print('\033[31mObs.:\033[mDesde que não morra nenhum coelho...')