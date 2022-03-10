import math
v = int(input('Qual é o valor do seu \033[4;34mângulo em graus\033[m? '))
r = math.radians(v)
print('O seu seno é \033[32m{:.2f}\033[m, seu cosseno é \033[32m{:.2f}\033[m e sua tangente é \033[32m{:.2f}\033[m'
      .format(math.sin(r), math.cos(r), math.tan(r)))
