num = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}o. valor:'))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
num.append(pares[:])
num.append(impares[:])
num[0].sort()
num[1].sort()
print(40 * '=-')
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
