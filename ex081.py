valores = list()
while True:
    n = int(input('Digite um valor:'))
    valores.append(n)
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print(30 * '-=')
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem descresente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')