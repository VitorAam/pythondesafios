f = str(input('Escreva uma \033[4;32mfrase\033[m qualquer: ')).upper().strip()
find = f.count('A')
local = f.find('A')+1
localf = f.rfind('A')+1
print("""Na sua frase, existem \033[34m{} letras "a"\033[m.
\033[34mA primeira letra "a"\033[m aparece no caractere nº {}
\033[34mA última letra "a"\033[m aparece no caractere nº {}""".format(find, local, localf))
