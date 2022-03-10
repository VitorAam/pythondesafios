from random import randint
me = ma = 0
n = randint(1, 10), randint(1, 10), randint(1, 10),\
    randint(1, 10), randint(1, 10)
for x, c in enumerate(n):
    if x == 0 or c < me:
        me = c
    if c > ma:
        ma = c
print(f'''Os valores sorteados foram: {n}
O maior valor sorteado foi {ma}
O menor valor sorteado foi {me}''')