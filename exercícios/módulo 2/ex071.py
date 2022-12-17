print(40 * '=')
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print(40 * '=')
while True:
    valor = int(input('Qual valor você quer sacar? R$'))
    valor1 = valor // 50
    valor2 = (valor % 50) // 20
    valor3 = ((valor % 50) % 20) // 10
    valor4 = (((valor % 50) % 20) % 10) // 1
    if valor1 != 0:
        print(f'Total de {valor1} cédulas de R$50,00')
    if valor % 50 != 0 and valor2 != 0:
        print(f'Total de {valor2} cédulas de R$20,00')
    if ((valor % 50) % 20) != 0 and valor3 != 0:
        print(f'Total de {valor3} cédulas de R$10,00')
    if (((valor % 50) % 20) % 10) != 0 and valor4 != 0:
        print(f'Total de {valor4} cédulas de R$1,00')
    if ((((valor % 50) % 20) % 10) % 1) == 0:
        break
print('Volte sempre ao Banco CEV! Tenha um bom dia!')
