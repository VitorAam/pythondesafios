casa = float(input('Qual o valor da casa a ser comprada? '
                   '\033[32mR$\033[m'))
salario = float(input('Qual é o seu salário atualmente? '
                      '\033[32mR$\033[m'))
anos = int(input('Em quantos anos você vai pagar a casa? '))
prestacao = casa/(anos*12)
if prestacao > (salario/100 * 30):
    print('Infelizmente esse empréstimo foi \033[31mnegado\033[m, '
          'não há compatibilidade com seu salário atual e o valor da parcela de {}.'.format(prestacao))
else:
    print('Esse empréstimo foi \033[34mAPROVADO\033[m! Providenciaremos o contrato dentro dos próximos dias.')
    