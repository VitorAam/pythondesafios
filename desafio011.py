a = float(input('Quantos metros de \033[31maltura\033[m tem sua parede? '))
l = float(input('Quantos metros de \033[31mlargura\033[mtem sua parede? '))
print('Serão necessários \033[4;34m{} litros\033[m de tinta para pintar sua parede!'.format(a*l/2))
