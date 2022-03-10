def voto(a=0):
    """
    Função para verificação de voto no sistema eleitoral brasileiro.
    a = ano de nascimento para verificação.
    """
    from datetime import datetime
    idade = datetime.today().year - a
    if 70 > idade > 18:
        situation = 'Voto OBRIGATÓRIO!'
    elif idade < 16:
        situation = 'Voto NEGADO!'
    else:
        situation = 'Voto OPCIONAL!'
    resposta = f'Com {idade} anos: {situation}.'
    return resposta


# programa principal
r = voto(int(input('Ano de nascimento: ')))
print(f'{r}')