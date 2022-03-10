s = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s += c
        cont += 1
print('A soma de todos os números ímpares múltiplos '
      'de 3 (total de {}),\ncompreendidos entre os números 1 e 500 é igual a {}'.format(cont, s))
