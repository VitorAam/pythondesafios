from random import randint
from time import sleep
d = randint(1, 10)
print('\033[1;33m-=-\033[m'*20)
print('\033[31mVou pensar em um número entre 1 e 10. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m'*20)
r = int(input('Em que número estou pensando? '))
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
if r != d:
    print('\033[31mGANHEI, HA HA HA!\033[m.')
elif r == d:
    print('\033[1;36mÉ...você acertou, não gostei..\033[m')
