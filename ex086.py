matriz = []
dados1 = []
dados2 = []
dados3 = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]:'))
    dados1.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]:'))
    dados2.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]:'))
    dados3.append(n)
matriz.append(dados1[:])
matriz.append(dados2[:])
matriz.append(dados3[:])
print(20 * '=-')
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')


