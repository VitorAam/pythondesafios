def leiaint(msg):
    while True:
        try:
            j = int(input(msg))
        except ValueError:
            print('\033[31mValor digitado não corresponde a um número inteiro.'
                  ' Por favor, digite um número inteiro:\033[m')
        except KeyboardInterrupt:
            print('O usuário não digitou os dados.')
            return 0
        else:
            return j


def linha(tam=42):
    return '_'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc
