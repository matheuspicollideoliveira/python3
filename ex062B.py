#JEITO DO PROFESSOR
print(40 * '=')
print('{:^40}'.format('TERMOS DE UMA PA'))
print(40 * '=')
p = int(input('Primeiro termo:'))
r = int(input('Razão:'))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + r
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos você quer mostrar? '))
print(f'Progressão finalizada com {total} termos mostrados!')

