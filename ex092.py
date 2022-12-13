from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome:'))
anonasc = int(input('Ano de nascimento:'))
cadastro['Idade'] = date.today().year - anonasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem):'))
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação:'))
    cadastro['Salário'] = float(input('Salário: R$ '))
    anoap = cadastro['Ano de contratação'] + 35
    cadastro['Aposentadoria'] = anoap - anonasc
print(30 * '-')
for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')