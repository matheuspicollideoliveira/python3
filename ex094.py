cadastro = dict()
ficha = list()
soma = media = mulheres = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome:'))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('Erro! Responda apenas M ou F!')
    cadastro['idade'] = int(input('Idade:'))
    ficha.append(cadastro.copy())
    while True:
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if r in 'SN':
            break
        print('Erro! Responda apenas S ou N!')
    if r in 'N':
        break
print(f'- O grupo tem {len(ficha)} pessoas!')
for e in ficha:
    soma += e["idade"]
media = soma / len(ficha)
print(f'- A média de idade é de {media:.2f} anos')
print('- As mulheres cadastras foram:', end=' ')
for e in ficha:
    if e['sexo'] in "F":
        print(f'[{e["nome"]}]', end=' ')
print('\n- Lista de pessoas que estão acima da média:')
for e in ficha:
    if e['idade'] > media:
        for k, v in e.items():
            print(f'  {k} = {v}', end=' ')
        print()
print('<<ENCERRADO>>')


