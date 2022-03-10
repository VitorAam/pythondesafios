from datetime import date
from time import sleep
print('Programa para alistamento obrigatório.')
sleep(1.5)
m = str(input('Você é do sexo masculino? ')).strip().lower()
idade = 18
if m == 'sim':
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    if idade > 18:
        print('Você já passou do tempo do alistamento em {} anos, se aliste!'.format(idade-18))
    elif idade == 18:
        print('Se aliste ainda esse ano para que não tenha pendências com o exercíto brasileiro!')
    elif idade < 18:
        print('Ainda faltam {} anos para você poder se alistar!'.format(18-idade))
elif m == 'não':
    print('Não há obrigatoriedade no alistamento militar, nesse caso!')

    