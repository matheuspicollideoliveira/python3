n = int(input('Digite um número inteiro para calcular seu fatorial:'))
c = n
fatorial = 1
print(f'\33[35mCalculando {n}! = \33[m',end='')
while c > 0:
    print(f'{c} ', end='')
    print('x' if c > 1 else '=', end=' ')
    fatorial = fatorial * c
    c = c - 1
print(f'\33[1:32m{fatorial}!\33[m')
#ou
n = int(input('Digite um número inteiro:'))
f = 1
for c in range(n, 1, -1):
    f = f * c
print(f)


