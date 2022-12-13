matriz = []
dados1 = []
dados2 = []
dados3 = []
total = soma0 = soma1 = soma2 = tot = cont = maior = 0
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]:'))
    dados1.append(n)
    if n % 2 == 0:
        soma0 += n
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]:'))
    dados2.append(n)
    if n % 2 == 0:
        soma1 += n
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]:'))
    dados3.append(n)
    if n % 2 == 0:
        soma2 += n
total = soma0 + soma1 + soma2
matriz.append(dados1[:])
matriz.append(dados2[:])
matriz.append(dados3[:])
print(20 * '=-')
for c in range(0, 3):
    tot += matriz[c][2]
for c in range(0, 3):
    if matriz[1]:
        if c == 0:
            maior = matriz[1][cont]
        else:
            if matriz[1][cont] > maior:
                maior = matriz[1][cont]
        cont += 1
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print(20 * '=-')
print(f'A soma dos valores pares é {total}!')
print(f'A soma dos valores da terceira coluna é {tot}!')
print(f'O maior valor da segunda linha é {maior}!')




