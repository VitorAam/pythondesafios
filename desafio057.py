sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo com somente [M] ou [F]: ')).upper().strip()
print('Sexo {} registrado, obrigado!'.format(sexo))
