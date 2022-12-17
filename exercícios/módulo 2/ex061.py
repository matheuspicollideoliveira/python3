print(40 * '=')
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print(40 * '=')
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
pa = 0
while pa < 10:
    print(p + r * pa,end=' -> ')
    pa +=1
print('FIM')

#ou

print(40 * '=')
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print(40 * '=')
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
termo = p
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo = termo + r
    cont += 1
print('FIM')


