n1 = float(input('Qual foi sua nota da primeira unidade? '))
n2 = float(input('Qual foi sua nota da segunda unidade? '))
m = (n1 + n2)/2
if m < 5.0:
    print('Infelizmente você foi reprovado. Sua nota na média foi {}'.format(m))
elif m > 7.0:
    print('Você foi aprovado! Parabéns! Sua nota foi {}'.format(m))
else:
    print('Você está na recuperação, sua nota foi {} estude bastante para ter uma boa prova!'.format(m))