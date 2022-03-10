from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('\033[32mAnalisando os valores para descobrir o maior...\033[m')
sleep(1)
if n1 > n2:
    print('O primeiro valor é maior que o segundo.')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')