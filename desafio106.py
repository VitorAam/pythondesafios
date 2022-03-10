def ajuda():
    """
    =>Função de help() personalizada, com transformação mais intuitiva para o usuário.
    """
    from time import sleep
    msg = 'SISTEMA DE AJUDA PyHELP'
    msg2 = 'Acessando o manual do comando'
    msg_fim = 'ATÉ LOGO!'
    while True:
        print('\033[;42m', '~'*(len(msg)+4), msg, '~'*(len(msg)+4), '\033[m')
        aux = str(input('Função ou Biblioteca > ')).strip()
        sleep(.3)
        if aux == 'fim':
            print('\033[;41m', end='')
            print('~'*(len(msg_fim)+4))
            print(f'  {msg_fim}')
            print('~'*(len(msg_fim)+4))
            print('\033[m')
            break
        print('\033[;44m', end='')
        print('~'*(len(msg2)+len(aux)+6))
        print(f"  {msg2} '{aux}'")
        print('~'*(len(msg2)+len(aux)+6))
        print('\033[m', end='')
        sleep(2.0)
        print('\033[;40;7m')
        help(aux)
        print('\033[m', end='')
        sleep(0.8)


# programa principal
ajuda()
