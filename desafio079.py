num = []
while True:
    novo = int(input('Digite um valor: '))
    if novo in num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        num.append(novo)
        print('Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=-'*20)
print(f'Você digitou os valores {num}')
