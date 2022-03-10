n1 = float(input('Digite um \033[32mnúmero\033[m: '))
n2 = float(input('Digite \033[34moutro número\033[m: '))
n3 = float(input('Digite um \033[33múltimo número\033[m: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O \033[31mmaior\033[m número é: \033[35m{}\033[m'.format(maior))
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O \033[31mmenor\033[m número é: \033[35m{}\033[m'.format(menor))
