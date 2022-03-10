nomenota = []
notas = []
composto = []
while True:
    name = str(input('Nome: ')).capitalize().strip()
    nomenota.append(name)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    media = (n1+n2)/2
    nomenota.append(notas[:])
    notas.clear()
    nomenota.append(media)
    composto.append(nomenota[:])
    nomenota.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-='*18)
print('No.  NOME {:>23}'.format('MÉDIA'))
print('-'*35)
for c in range(len(composto)):
    print('{:<5}{:<18}{:>10}'.format(c, composto[c][0], composto[c][2]))
print('-'*35)
while True:
    sel = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if sel == 999:
        break
    else:
        print(f'Notas de {composto[sel][0]} são {composto[sel][1]}')
    print('_'*35)
print('FINALIZANDO...')
print('VOLTE SEMPRE')
