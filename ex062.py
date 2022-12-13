print(40 * '=')
print('{:^40}'.format('TERMOS DE UMA PA'))
print(40 * '=')
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
pa2 = 0
pa = 0
while pa < 10:
    print(p + r * pa, ' -> ', end='')
    pa += 1
print('PAUSA')
t = int(input('\nQuer que mostre mais quantos termos?'))
while pa2 < t:
    print((p + r * 10) + r * pa2,end='-> ')
    pa2 += 1
    if t == 0:
        print('FIM')
print('FIM')






