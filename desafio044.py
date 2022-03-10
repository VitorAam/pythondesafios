from time import sleep
p = float(input('Preço das compras '
                '\033[32mR$\033[m'))
print('''Escolha o metódo de pagamento:
[1] para pagamento à vista em dinheiro ou cheque
[2] para pagamento à vista no cartão
[3] para pagamento em até 2x no cartão
[4] para pagamento em 3x ou mais no cartão''')
sleep(1.5)
m = int(input('Qual o número para metódo de pagamento? '))
if m == 1:
    print('O valor das compras tem 10% de desconto, ficando por R${:.2f}'.format(p-p*0.10))
elif m == 2:
    print('O valor das compras tem 5% de desconto, ficando por R${:.2f}'.format(p-p*0.05))
elif m == 3:
    print('O valor das compras é o padrão, de R${:.2f}'.format(p))
elif m == 4:
    print('O valor das compras fica 20% mais caro, ficando por R${:.2f}'.format(p+p*0.2))
else:
    print('OPÇÃO INVÁLIDA de pagamento! Tente novamente...')
    