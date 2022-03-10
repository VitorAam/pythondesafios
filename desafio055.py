menor = 0
maior = 0
for c in range(1, 6):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menor = p
        maior = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print('A pessoa com o maior peso tem {}Kg, a pessoa com menor peso tem {}Kg'.format(maior, menor))
