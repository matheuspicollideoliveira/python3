matriz = []
dados = []
pares = []
coluna3 = []
linha2 = []
soma = tot = maior = 0
for c in range(0, 3):
    for x in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{c}, {x}]:')))
        if dados[x] % 2 == 0:
            pares.append(dados[x])
        if x == 2:
            coluna3.append(dados[2])
        if c == 1:
            linha2.append(dados[x])
    matriz.append(dados[:])
    dados.clear()
for p in range(0, len(pares)):
    soma += pares[p]
for p in range(0, len(coluna3)):
    tot += coluna3[p]
for p in range(0, len(linha2)):
    if p == 0:
        linha2[p] = maior
    else:
        if linha2[p] > maior:
            maior = linha2[p]
for p in range(0, 3):
    for t in range(0, 3):
        print(f'[ {matriz[p][t]} ]', end=' ')
    print()
print(f'A soma dos valores pares é {soma}!')
print(f'A soma dos valores da terceira coluna é {tot}!')
print(f'O maior valor da segunda linha é {maior}!')
