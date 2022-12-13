galera = list()
dados = list()
tot = maior = menor = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    galera.append(dados[:])
    dados.clear()
    if tot == 0:
        maior = menor = galera[tot][1]
    else:
        if galera[tot][1] > maior:
            maior = galera[tot][1]
        elif galera[tot][1] < menor:
            menor = galera[tot][1]
    tot += 1
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print(40 * '=-')
print(f'Ao todo, você cadastrou {tot} pessoas!')
print(f'O maior peso foi de {maior} Kg. Peso de', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0].upper()}]', end=' ')
print(f'\nO menor peso foi de {menor} Kg. Peso de', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0].upper()}]', end=' ')
