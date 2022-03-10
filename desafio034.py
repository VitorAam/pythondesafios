s = float(input('Digite o \033[34mvalor\033[m do seu salário \033[32mR$\033[m'))
if s > 1250.00:
    print('Seu aumento foi de \033[4;34m10%\033[m, seu novo salário é de \033[32mR${}\033[m'.format(s+(s/100*10)))
else:
    print('Seu aumento foi de \033[4;34m15%\033[m, seu novo salário é de \033[32mR${}\033[m'.format(s+(s/100*15)))