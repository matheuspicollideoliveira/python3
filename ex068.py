from random import randint
print(20 * '-=')
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print(20 * '-=')
cont = 0
while True:
    n = int(input('Digite um valor? '))
    escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    computador = randint(0, 10)
    print(40 * '-')
    total = n + computador
    if total % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {total} DEU PAR')
    else:
        print(f'Você jogou {n} e o computador jogou {computador}. Total de {total} DEU ÍMPAR')
    print(40 * '-')
    if escolha in 'Pp' and total % 2 == 0:
        print('\33[1:32mVocê VENCEU\33[m')
        print('Vamos jogar novamente...')
        print(20 * '-=')
        cont += 1
    elif escolha in 'Ii' and total % 2 != 0:
        print('\33[1:32mVocê VENCEU\33[m')
        print('Vamos jogar novamente...')
        print(20 * '-=')
        cont += 1
    else:
        print('\33[1:31mVocê PERDEU\33[m')
        break
print(f'GAME OVER! Você venceu {cont} vezes!')