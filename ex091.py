from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
print('\33[36mValores sorteados:\33[m')
for c in range(0, 4):
    jogadores[f'jogador{c+1}'] = randint(1, 6)
for k, v in jogadores.items():
    sleep(0.8)
    print(f'O {k} tirou {v} no dado.')
print(30 * '-')
print('\33[32mRaking dos jogadores:\33[m')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.8)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

