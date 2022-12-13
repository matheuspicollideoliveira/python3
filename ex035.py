print('-'*20)
print('Analisador de triângulos')
print('-'*20)
r1 = float(input('Reta 1:'))
r2 = float(input('Reta 2:'))
r3 = float(input('Reta 3:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo com o comprimento das retas acima!!!')
else:
    print('Não é possível formar um triângulo com o comprimento das retas acima!')
