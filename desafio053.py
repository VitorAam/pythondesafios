f = str(input('Digite uma frase para descobrirmos se ela é um palíndromo: ')).strip().lower().replace(' ', '')
print('A frase: {} ao inverso é: {}'.format(f, f[::-1]))
if f == f[::-1]:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo!')