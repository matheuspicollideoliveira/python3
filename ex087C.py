matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for c in range(0, 3):
    for x in range(0, 3):
        matriz[c][x] = int(input(f'Digite um valor para [{c}, {x}]:'))
print(20 * '=-')
for p in range(0, 3):
    for t in range(0, 3):
        print(f'[ {matriz[p][t]:^5} ]', end=' ')
        if matriz[p][t] % 2 == 0:
            spar += matriz[p][t]
    print()
for c in range(0, 3):
    scol += matriz[c][2]
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'A soma dos valores pares é {spar}!')
print(f'A soma dos valores da terceira coluna é {scol}!')
print(f'O maior valor da segunda linha é {mai}!')
