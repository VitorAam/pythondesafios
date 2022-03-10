from time import sleep


def maior(* num):
    m = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
        if v > m:
            m = v
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')
    sleep(0.2)


maior(2, 9, 4, 5, 6, 7)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
