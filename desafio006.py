n1 = float(input('Digite um número: '))
print('O dobro do seu número é \033[4;36m{}\033[m, '
      'o seu triplo é \033[4;36m{}\033[m e sua raiz quadrada é '
      '\033[4;36m{:.2f}\033[m'.format(n1*2, n1*3, n1**(1/2)))
