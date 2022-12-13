val = list()
while True:
    v = int(input('Digite um valor:'))
    if v not in val:
        val.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado...Não vou adicionar!')
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    while r not in 'SN':
        r = str(input('Tente novamente...Quer continuar? [S/N]')).strip().upper()
    if r in 'N':
        break
val.sort()
print(f'Você digitou os valores {val}')

