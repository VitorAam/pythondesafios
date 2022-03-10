print('_'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('_'*50)
lista = ('Garrafa', 30.00, 'Teclado', 315.00, 'Monitor', 1457.99,
         'Caderno', 23.50, 'Caneta', 8.00, 'Notebook', 4300.00,
         'Cabos', 15.00, 'Playstation 4', 1350.00, 'Livro', 58.00)
for x, c in enumerate(lista):
    if c == lista[-1]:
        print('_'*50)
    elif x == 0:
        print('{:.<40}R${:>8}'.format(c, lista[x+1]))
    elif x % 2 == 0:
        print('{:.<40}R${:>8}'.format(c, lista[x+1]))
