p = float(input('Qual o \033[31mpreço\033[m do produto? \033[32mR$\033[m'))
print('Com nosso \033[31mdesconto\033[m de pagamento antecipado ele vai ficar por \033[32mR${:.2f}\033[m'.format(p-(p/100*5)))
