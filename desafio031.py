v = float(input('Qual a \033[33mdistância\033[m da sua viagem em \033[32mKm\033[m? '))
if v <= 200:
    print('O \033[35mvalor\033[m da sua passagem vai ser de \033[32mR${}\033[m'.format(v*0.5))
else:
    print('O \033[35mvalor\033[m da sua passagem vai ser de \033[32mR${}\033[m'.format(v*0.45))