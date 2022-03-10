def notas(* num, sit=False):
    """
    =>Função para análise de notas de vários alunos
    :param num: Notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação das notas
    :return: dicionário com várias informações sobre a situação das notas.
    """
    print('-'*85)
    ma = me = med = 0
    dicionario = dict()
    for v, c in enumerate(num):
        if v == 0:
            ma = c
            me = c
        if c < me:
            me = c
        elif c > ma:
            ma = c
        med += c
    media = med / len(num)
    dicionario['Total'] = len(num)
    dicionario['Maior'] = ma
    dicionario['Menor'] = me
    dicionario['Média da turma'] = media
    if sit:
        if dicionario['Média da turma'] >= 7:
            dicionario['Situação'] = 'BOA'
        elif dicionario['Média da turma'] >= 5:
            dicionario['Situação'] = 'RAZOÁVEL'
        else:
            dicionario['Situação'] = 'RUIM'
    return dicionario


# programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
