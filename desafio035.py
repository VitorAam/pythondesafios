print('\033[33m-=-\033[m'*10)
print('\033[35mAnalisador de triângulos\033[m')
print('\033[33m-=-\033[m'*10)
r1 = float(input('Digite o valor da \033[32mprimeira reta\033[m: '))
r2 = float(input('Digite o valor da \033[32msegunda reta\033[m: '))
r3 = float(input('Digite o valor da \033[32mterceira reta\033[m: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mÉ possível\033[m formar um triângulo com esses valores!')
else:
    print('\033[31mNão é possível\033[m formar um triângulo com esses valores.')
