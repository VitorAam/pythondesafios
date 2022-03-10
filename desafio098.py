from time import sleep


def linha():
    print('-=' * 30)


def contador(a, b, c):
    linha()
    if c == 0:
        c = 1
    elif c < 0:
        c *= (-1)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    n = a
    print(n, end=' ')
    sleep(0.3)
    if b < a:
        c *= (-1)
    n += c
    while a < n < b or a > n > b:
        print(n, end=' ')
        n += c
        sleep(0.3)
    if n == b:
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')
    sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim:    ')), int(input('Passo:  ')))
