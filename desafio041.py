from datetime import date
from time import sleep
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
sleep(1)
a = int(input('Qual o ano de nascimento do atleta? '))
i = date.today().year - a
if i <= 9:
    print('Esse atleta é da categoria MIRIM.')
elif i <= 14:
    print('Esse atlteta é da categoria INFANTIL.')
elif i <= 19:
    print('Esse atleta é da categoria JUNIOR.')
elif i <= 20:
    print('Esse atleta é da categoria SÊNIOR.')
else:
    print('Esse atleta é da categoria MASTER.')
