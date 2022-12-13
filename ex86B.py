matriz = []
dados = []
for c in range(0, 3):
    for x in range(0, 3):
        dados.append(int(input(f'Digite um valor para [{c}, {x}]:')))
    matriz.append(dados[:])
    dados.clear()
print(20 * '=-')
for p in range(0, 3):
    for t in range(0, 3):
        print(f'[ {matriz[p][t]:^5} ]', end=' ')
    print()
