print('='*30)
print('{:^30}'.format('BANCO GG'))
print('='*30)
v = float(input('Que valor você quer sacar? R$'))
cinquenta = vinte = dez = um = 0
while True:
    if v > 50.00:
        cinquenta = v // 50.00
        v = v - (50*cinquenta)
    elif v > 20.00:
        vinte = v // 20.00
        v = v - (20*vinte)
    elif v > 10.00:
        dez = v // 10.00
        v = v - (10*dez)
    elif v > 1:
        um = v // 1.00
        v = v - (1*um)
    else:
        break
print('''Total de {:.0f} cédulas de R$50
Total de {:.0f} cédulas de R$20
Total de {:.0f} cédulas de R$10
Total de {:.0f} cédulas de R$1'''.format(cinquenta, vinte, dez, um))
print('='*30)
print('Volte sempre ao BANCO GG! Tenha um bom dia!')
