from datetime import date
ano = int(input('Digite o seu ano de nascimento:'))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos e está na categoria JUNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria SENIOR!')
else:
    print(f'Você tem {idade} anos e está na categoria MASTER!')