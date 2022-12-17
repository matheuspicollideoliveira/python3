import random
from time import sleep
num = random.randint(0, 5) #faz o computador pensar
print('-'*55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-'*55)
n = int(input('Em que número eu pensei?')) #verifica o número do jogador
print('\33[0;35mPROCESSANDO...')
sleep(1) #quantos segundos ele espera
if num == n:
    print('\33[0:32mParabéns você conseguiu me vencer!')
else:
    print(f'\33[0:31mVocê perdeu, eu pensei no número {num} e não no {n}!')
