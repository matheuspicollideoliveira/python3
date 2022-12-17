s = float(input('Digite seu salário em R$:'))
if s > 1250:
    salario = s * 1.10
else:
    salario = s * 1.15
print(f'Seu salário com aumento é R${(salario):.2f}!')
