listageral = []
listapar = []
listaimpar = []
resposta = 'S'
while resposta != 'N':
    numero = int(input('Digite um valor: '))
    listageral.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    resposta = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
print(f'''Os números digitados foram:{listageral}
Os números pares são: {listapar}
Os números ímpares são: {listaimpar}''')
