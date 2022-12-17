print(40 * '=')
print('{:^40}'.format('NÚMERO PRIMO'))
print(40 * '=')
num = int(input('Digite um número inteiro:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[1:33m',end='')
        tot += 1
    else:
        print('\33[0:31m',end='')
    print(f' {c} ', end='')
print(f'\n\33[mO número {num} foi dívisível {tot} vezes!')
if tot == 2:
    print('\33[1:32mE por isso ele é PRIMO!')
else:
    print('\33[31mE por isso ele NÃO É PRIMO!')