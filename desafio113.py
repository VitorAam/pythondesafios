def leiaint(msg):
    print('_' * 30)
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


def leiafloat(msg):
    print('_'*30)
    while True:
        try:
            v = input(msg).replace(',', '.')
            v = float(v)
        except ValueError:
            print('\033[31mERRO! Tente novamente, utilize um número real.\033[m')
        except KeyboardInterrupt:
            print('O usuário não digitou os dados.')
            return 0
        else:
            return v


a = leiaint('Digite um Inteiro: ')
b = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {a} e o real foi {b}')
