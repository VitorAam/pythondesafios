from datetime import date
a = int(input('Qual \033[4;32mo ano\033[m que você quer analisar? Coloque '
              '\033[31m0\033[m para analisar \033[4;32mo ano atual\033[m: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Esse ano é \033[36mBISSEXTO\033[m!')
else:
    print('Esse ano \033[31mNÃO\033[m é \033[36mBISSEXTO\033[m!')
    