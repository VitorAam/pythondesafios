import math
c1 = float(input('Qual o comprimento do \033[34mcateto adjacente\033[m? Apenas números '))
c2 = float(input('Qual o comprimento do \033[32mcateto oposto\033[m? Apenas números '))
print('O valor da \033[35mhipotenusa\033[m é igual a: {:.2f}'.format(math.hypot(c1, c2)))
