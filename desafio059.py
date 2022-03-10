from time import sleep
print('-=-'*7)
print('{:-^20}'.format('OPERANDO COM NÚMEROS'))
print('-=-'*7)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
selecionado = 0
maior = n1
if n2 > maior:
    maior = n2
while selecionado != 5:
    print('-=-'*15)
    selecionado = int(input('''Selecione:
    [1] para somar
    [2] para multiplicar
    [3] para verificar o maior valor
    [4] para mudar os números da operação
    [5] para sair do programa
    
>>>>Selecionado: '''))
    if selecionado == 1:
        print('A soma dos valores é igual a {}'.format(n1 + n2))
    elif selecionado == 2:
        print('A multiplicação dos valores é igual a {}'.format(n1 * n2))
    elif selecionado == 3:
        print('O maior valor, dentre os digitados é {}'.format(maior))
    elif selecionado == 4:
        n1 = float(input('Digite um novo valor: '))
        n2 = float(input('Digite um segundo novo valor: '))
    elif selecionado == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(2)

print('-=-'*15)
print('Fim do programa! Volte sempre!')
