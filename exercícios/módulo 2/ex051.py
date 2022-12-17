print(40 * '=')
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print(40 * '=')
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
for c in range(p, p + (r * 10), r):
    print(f'{c}', end=' -> ')
print('ACABOU')
