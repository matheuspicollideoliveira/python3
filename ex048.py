soma = 0
cont = 0
print('Somatório dos múltiplos de 3 entre 1 e 500:')
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}!')


