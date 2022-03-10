def leiaint(msg):
    print('_' * 30)
    v = input(msg)
    while v.isnumeric() is False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        v = input('Digite um número: ')
    return v


# programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
