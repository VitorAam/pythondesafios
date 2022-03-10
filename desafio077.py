palavras = ('Estou', 'Aprendendo', 'Programação',
            'Na', 'Velocidade', 'Que', 'Tenho', 'Condições',
            'Espero', 'Conseguir', 'Aprender', 'Bastante')
for p in palavras:
    print(f'Na palavra {p.upper()} temos:', end=' ')
    for l in range(0, len(p)):
        if p[l] in 'AaEeIiOoUu':
            print(p[l].lower(), end=' ')
    print()
