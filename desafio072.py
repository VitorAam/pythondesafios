numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while 0 > n1 or n1 > 20:
    n1 = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[n1]}!')
while True:
    resposta = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'S':
        n1 = int(input('Digite outro número entre 0 e 20: '))
        print(f'Você digitou o número {numeros[n1]}!')
    elif resposta == 'N':
        print('Ok! Obrigado por utilizar o programa!')
        break
    else:
        resposta = str(input('Resposta inválida, use somente [S] ou [N]'))

