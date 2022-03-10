n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número inteiro para somar, digite "999" para finalizar a soma: '))
    s += n
    c += 1
print('A soma de todos os números digitados'
      ' é igual a {} e foram digitados {} números.'.format(s-999, c-1))
