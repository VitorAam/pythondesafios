lista = []
resposta = 'S'
while resposta != 'N':
    n = int(input('Adicione um valor: '))
    lista.append(n)
    resposta = str(input('Você quer digitar outro valor? [S/N] ')).upper().strip()[0]
if 5 in lista:
    print(f'O número 5 foi digitado na lista, ele aparece na posição {lista.index(5)}')
else:
    print('O número 5 não foi digitado.')
lista.sort(reverse=True)
print(f'''Foram digitados {len(lista)} números.
A lista de valores, ordenada em forma decrescente é: {lista}''')

