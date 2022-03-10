v = float(input('Qual foi a \033[34mvelocidade do carro\033[m em km/h? '))
if v > 80:
    print('Esse carro foi \033[31mMULTADO\033[m, o valor da multa é de \033[32mR${}\033[m.'.format((v-80)*7))
else:
    print('\033[36mVelocidade permitida!\033[m')
print('--FIM--')
