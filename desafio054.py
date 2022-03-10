from datetime import date
ano = date.today().year
ma = 0
me = 0
for c in range(0, 7):
    i = int(input('Em que ano você nasceu? '))
    if ano - i >= 21:
        ma = ma + 1
    else:
        me = me + 1
print('Nesse grupo existem {} pessoas maiores de idade e {} menores de idade.'.format(ma, me))
