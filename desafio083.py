expr = str(input('Digite a expressão: '))
conjunto = []
for simb in expr:
    if simb == '(':
        conjunto.append('(')
    elif simb == ')':
        if len(conjunto) > 0:
            conjunto.pop()
        else:
            conjunto.append(')')
            break
if len(conjunto) == 0:
    print('A expressão é VÁLIDA!')
else:
    print('A expressão é INVÁLIDA!')
