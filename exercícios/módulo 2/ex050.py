soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro:'))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f'A soma dos {cont} números pares é {soma}!')
