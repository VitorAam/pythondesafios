print('_'*30)
print('{:^30}'.format('LOJA ATACADÃO'))
print('-'*30)
c = s = mb = cp = 0
n1 = ''
while True:
    n = str(input('Nome do produto: ')).upper()
    p = float(input('Preço do produto: R$'))
    s += p
    cp += 1
    if cp == 1 or p < mb:
        mb = p
        n1 = n
    if p > 1000.00:
        c += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja adicionar outro produto? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        print('Agradecemos!')
        break
print(f'O valor total da compra foi R${s}')
print(f'No seu carrinho existem no total de {c} produtos acima de R$1000,00')
print(f'O produto mais barato do seu carrinho é: {n1}')
