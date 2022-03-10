linhas = []
colunas = []
c = d = pares = coluna3 = 0
for l in range(0, 3):
    for a in range(0, 3):
        v = int(input(f'Digite um valor para [{l}, {a}]: '))
        if v % 2 == 0:
            pares += v
        colunas.append(v)
        if a == 2:
            coluna3 += v
    linhas.append(colunas[:])
    colunas.clear()
print('-='*40)
for li in linhas:
    for co in range(0, 3):
        print(f'[  {linhas[c][d]}  ]', end='')
        d += 1
    print()
    c += 1
    d = - d
print('-='*40)
linhas[1].sort()
print(f'''A soma dos valores pares da matriz é igual a: {pares}
A soma dos valores da terceira coluna da matriz é igual a: {coluna3}
O maior valor da segunda linha é: {linhas[1][-1]}''')
