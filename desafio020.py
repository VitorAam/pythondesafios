from random import shuffle
a1 = input('Digite o nome do \033[31mprimeiro aluno\033[m: ')
a2 = input('Digite o nome do \033[35msegundo aluno\033[m: ')
a3 = input('Digite o nome do \033[34mterceiro aluno\033[m: ')
a4 = input('Digite o nome do \033[32mquarto aluno\033[m: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Os alunos irão apresentar o trabalho na \033[33mseguinte ordem\033[m:', lista)
