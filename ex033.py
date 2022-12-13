n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))
n3 = float(input('Terceiro número:'))
#verificando menor valor
menor = n1
if n2 < n1 and n3 > n2:
    menor = n2
if n3 < n1 and n2 > n3:
    menor = n3
#verificando maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitadado foi {menor}!')
print(f'O maior valor digitado foi {maior}!')

