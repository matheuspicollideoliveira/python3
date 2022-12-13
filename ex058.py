import random
cont = 1
computador = random.randint(0, 10)
print('-'*55)
print('''Sou seu computador...
Vou pensar em um número entre 0 e 10. Tente adivinhar...''')
print('-'*55)
n = int(input('\33[33mEm que número eu pensei?\33[m'))
while computador != n:
    if computador > n:
        print('Mais...Tente novamente.')
    else:
        print('Menos...Tente novamente.')
    n = int(input('\33[33mEm que número eu pensei?\33[m'))
    cont += 1
print(f'Parabénss!!! Você acertou e precisou de {cont} tentativas!')

