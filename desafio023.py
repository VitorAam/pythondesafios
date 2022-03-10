num = int(input('Informe um número: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print("""\033[34munidade\033[m:{}
\033[34mdezena\033[m:{}
\033[34mcentena\033[m:{}
\033[34mmilhar\033[m:{}""".format(u, d, c, m))