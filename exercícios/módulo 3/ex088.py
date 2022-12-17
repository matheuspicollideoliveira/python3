from random import randint
from time import sleep
print(30 * '-')
print('{:^30}'.format('JOGOS DA MEGA SENA'))
print(30 * '-')
jogos = list()
num = list()
j = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:=^30}'.format(f'SORTEANDO {j} JOGOS'))
for n in range(0, j):
    cont0 = 0
    while True:
        sorteio = randint(0, 60)
        if sorteio not in num:
            num.append(sorteio)
            cont0 += 1
        if cont0 >= 6:
            break
    num.sort()
    jogos.append(num[:])
    num.clear()
for i, p in enumerate(jogos):
    sleep(0.8)
    print(f'Jogo{i+1}: {p}')
print('{:=^30}'.format('< BOA SORTE >'))

