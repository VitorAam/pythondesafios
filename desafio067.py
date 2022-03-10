while True:
    n = int(input('Digite um número para ver sua tabuada (número negativo para parar): '))
    print('-=-' * 23)
    if n < 0:
        break
    for m in range(1, 11):
        print(f'{n} x {m} = {n*m}')
    print('-=-' * 23)
print('FIM DO PROGRAMA')
