n1 = float(input('Quantos metros você quer calcular? '))
print('Esse valor é igual a: \n \033[32m{}\033[mmm \n \033[32m{}\033[mcm'.format(n1*1000, n1*100))
print(' \033[32m{}\033[mdm \n'
      ' \033[32m{}\033[mm\n'
      ' \033[32m{}\033[mdam \n'
      ' \033[32m{}\033[mhm '
      '\n \033[32m{}\033[mkm'. format(n1*10, n1, n1/10, n1/100, n1/1000))
