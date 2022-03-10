nome = str(input('Qual é o seu \033[34mnome\033[m? ')).strip()
print('Seu nome tem \033[35mSilva\033[m? {}'.format('silva' in nome.lower()))
