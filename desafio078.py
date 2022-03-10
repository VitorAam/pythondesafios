num = []
me = ma = 0
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
    if c == 0:
        me = ma = num[c]
    else:
        if num[c] > ma:
            ma = num[c]
        if num[c] < me:
            me = num[c]
print(f'Os valores digitados foram: {num}')
print(f'O menor valor da lista foi {me} e ele está nas posições:', end=' ')
for i, v in enumerate(num):
    if v == me:
        print(f'{i}...', end='')
print()
print(f'O maior valor foi {ma} e ele está nas posições:', end=' ')
for j, m in enumerate(num):
    if m == ma:
        print(f'{j}...', end='')
