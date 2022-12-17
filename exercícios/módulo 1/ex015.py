d=int(input('Quantos dias alugados?'))
km=float(input('Quantos km rodados?'))
custo = (60*d) + (0.15*km)
print(f'O total a pagar é de R${(custo):.2f}!')
