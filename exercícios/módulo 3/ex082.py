num = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número:'))
    num.append(n)
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
for c, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')


'''for c in range(0, len(num)):
    if num[c] % 2 == 0:
        pares.append(num[c])
    else:
        impares.append(num[c])'''