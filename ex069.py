cont = cont2 = cont3 = 0
while True:
    print(30 * '-')
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print(30 * '-')
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print(30 * '-')
    if idade >= 18:
        cont +=1
    if sexo in 'Mm':
        cont2 += 1
    if sexo in 'Ff' and idade < 20:
        cont3 += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('{:=^32}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {cont2} homens cadastrados!')
print(f'E temos {cont3} mulheres com menos de 20 anos')