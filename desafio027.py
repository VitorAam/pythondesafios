n = input('\033[34mQual é o seu nome?\033[m ')
n1 = n.split()[0]
n2 = n.split()[-1]
print("""\033[4;32mPrimeiro\033[m nome: {}
\033[4;32mÚltimo\033[m nome: {}""".format(n1, n2))



