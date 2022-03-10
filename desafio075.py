num = int(input('Digite um valor: ')), \
      int(input('Digite outro valor: ')),\
      int(input('Digite mais um valor: ')),\
      int(input('Digite um último valor: '))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
tres = num.count(3)
if tres == 0:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 foi digitado na posição de número {num.index(3)+1}')
print('Os números pares foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')