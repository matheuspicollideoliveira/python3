'''n = int(input('Digite um número de 0 a 9999:'))
num = str(n)
print(f'Unidade:{num[3]}')
print(f'Dezena:{num[2]}')
print(f'Centena:{num[1]}')
print(f'milhar:{num[0]}')'''

#ou

num = int(input('Digite um número de 0 a 9999:'))
n = str(num)
u = (num//1)%10
d = (num//10)%10
c = (num//100)%10
m = (num//1000)%10
print(f'Analisando o número {num}:')
print(f'Unidade:{u}\nDezena:{d}\nCentena:{c}\nMilhar:{m}')
