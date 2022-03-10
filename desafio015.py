d = int(input('Quantos \033[4;34mdias\033[m você ficou com o carro alugado? '))
km = float(input('Quantos \033[4;34mKm\033[m foram rodados com ele? '))
print('O total a pagar é de \033[32mR${}\033[m'.format(d*60+km*0.15))
