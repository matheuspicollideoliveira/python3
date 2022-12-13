from random import randint
from time import sleep


def sorteia(list):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        list.append(randint(1, 10))
    for v in list:
        print(v, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    s = 0
    for c in range(0, len(lst)):
        if lst[c] % 2 == 0:
            s += lst[c]
    print(f'Somando os valores pares de {lst}, temos {s}')


valores = []
sorteia(valores)
somaPar(valores)



