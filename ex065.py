print(40 * '=')
print('{:^40}'.format('Maior, Menor e Média!'))
print(40 * '=')
r = 'Ss'
tot = 0
cont = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('\33[1:35mDigite um número:\33[m '))
    r = str(input('Quer continuar? \33[1:32m[S\33[m/\33[1:31mN]\33[m ')).strip()[0]
    tot += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = tot / cont
print(f'A média entre os {cont} valores digitados é de {media}!')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}!')