import random
a1 = input('Digite o \033[31mnome do aluno 1\033[m: ')
a2 = input('Digite o \033[35mnome do aluno 2\033[m: ')
a3 = input('Digite o \033[34mnome do aluno 3\033[m: ')
a4 = input('Digite o \033[32mnome do aluno 4\033[m: ')
lista = [a1, a2, a3, a4]
print('O \033[4;33maluno sorteado\033[m foi: {}'.format(random.choice(lista)))
