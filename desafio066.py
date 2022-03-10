c = s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    c += 1
    if n == 999:
        break
    s += n
print(f'Foram digitados no total de {c} números, a soma deles é igual a {s}!')
