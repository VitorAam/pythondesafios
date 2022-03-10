n1 = int(input('Digite um número para descobrir sua tabuada: '))
t = ('-'*15)
print("A tabuada desse número é: \n "
      "{0} \n {1} \033[31mx\033[m 1 = {2} \n {1} \033[31mx\033[m 2 = {3} "
      "\n {1} \033[31mx\033[m 3 = {4} \n {1} \033[31mx\033[m 4 = {5} \n {1} \033[31mx\033[m 5 = {6}"
      " \n {1} \033[31mx\033[m 6 = {7} \n {1} \033[31mx\033[m 7 = {8} \n {1} \033[31mx\033[m 8 = {9} \n"
      " {1} \033[31mx\033[m 9 = {10} \n {0}".format(t, n1, n1 * 1, n1 * 2, n1 * 3, n1 * 4, n1 * 5, n1 * 6, n1 * 7, n1 * 8, n1 * 9))
