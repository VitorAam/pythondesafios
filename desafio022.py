from time import sleep
nome = str(input('Qual é o \033[4;31mseu nome\033[m? ')).strip()
m = nome.upper()
n = nome.lower()
d = nome.split()
j = len(''.join(d))
n1 = len(d[0])
print('\033[mAnalisando seu nome...\033[m')
sleep(1)
print('O seu nome em \033[34mmaiúsculas\033[m fica: {}. \n'
      'O seu nome em \033[34mmínusculas\033[m fica: {}. \n'
      'O seu nome tem no \033[34mtotal de {} letras\033[m. \n'
      'A \033[34mprimeira palavra\033[m do seu nome tem {} letras.'.format(m, n, j, n1))
