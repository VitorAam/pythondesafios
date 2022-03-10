p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
IMC = p/a**2
print('Seu Índice de Massa Corporal é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso')
elif IMC < 25:
    print('Você está no peso ideal')
elif IMC < 30:
    print('Você está com sobrepeso')
elif IMC < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida, cuidado!')