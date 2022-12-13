valor = float(input('Digite o valor da casa:R$'))
salario = float(input('Digite o salário do comprador:R$'))
tempo = float(input('Digite o tempo de financiamento em anos:'))
prestacao = valor / (tempo * 12)
print(f'Para pagar uma casa de R${(valor):.2f} com um salário de R${(salario):.2f}\na prestação mensal será de R${(prestacao):.2f}! ',end = '')
if prestacao < (salario * 0.3):
    print('\33[32mEmpréstimo CONCEDIDO!\33[m')
else:
    print('\33[31mEmpréstimo NEGADO!\33[m')