def fatorial(a, show=False):
    """
    => Calcula o Fatorial (!) de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número a.
    """
    f = 1
    print('-'*30)
    if show is False:
        for c in range(a, 0, -1):
            f *= c
        return f
    elif show is True:
        for c in range(a, 0, -1):
            f *= c
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        return f


print(fatorial(4, True))
