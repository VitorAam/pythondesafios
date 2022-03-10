linhas = []
colunas = []
c = d = 0
for l in range(0, 3):
    for a in range(0, 3):
        v = int(input(f'Digite um valor para [{l}, {a}]: '))
        colunas.append(v)
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
