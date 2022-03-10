def sorteia():
    from random import randint
    from time import sleep
    print(f'Sorteando {len(lista)} valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        sleep(0.3)
        lista.append(n)
    print('PRONTO!')


def somapar():
    sp = 0
    for c in lista:
        if c % 2 == 0:
            sp += c
    print(f'A soma dos números pares dentro de {lista} é igual a {sp}')


# programa principal
lista = []
sorteia()
somapar()
