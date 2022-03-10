n = str(input('Qual é o \033[36mnome\033[m da sua \033[36mcidade\033[m? ')).strip()
divided = n.split()
n1 = divided[0]
n1 = n1.upper()
santo = 'SANTO' in n1
print('O nome da sua cidade começa com \033[31mSANTO\033[m? {}'.format(santo))

