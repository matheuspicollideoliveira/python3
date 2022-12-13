print('{:=^32}'.format('\33[36mTABUADA\33[m'))
num = int(input('Digite um número inteiro:'))
print(15 * '-')
for c in range(1, 11):
    print(f'{num} x {(c):2} = {num * c}')
print(15 * '-')
