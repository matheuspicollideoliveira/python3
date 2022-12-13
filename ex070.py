print(40 * '-')
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print(40 * '-')
tot = cont1000 = cont = menor = 0
maisbarato = ' '
while True:
    produto = str(input('\33[35mNome do produto: \33[m')).strip()
    preço = float(input('Preço: R$'))
    tot += preço
    cont += 1
    if cont == 1:
        menor = preço
        maisbarato = produto
    else:
        if preço < menor:
            menor = preço
            maisbarato = produto
    if preço > 1000:
        cont1000 += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('\33[36mQuer continuar? [S/N]\33[m')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${(tot):.2f}!')
print(f'Temos {cont1000} produtos custando mais de R$1000,00!')
print(f'O produto mais barato foi {maisbarato} que custa R${(menor):.2f}!')
