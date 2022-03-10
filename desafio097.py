def escreva(msg):
    print('~'*(len(msg)+2))
    print('{:^{}}'.format(msg, (len(msg)+2)))
    print('~'*(len(msg)+2))


# programa principal
escreva(msg=str(input('Escreva algo: ')))
