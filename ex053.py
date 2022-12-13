print(40 * '=')
print('{:^40}'.format('DETECTOR DE PALÍNDROMO'))
print(40 * '=')
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#poderia tirar as três próximas linhas e escrever:
#inverso = junto[::-1]
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}!')
if inverso == junto:
    print('\33[32mTemos um palíndromo!')
else:
    print('\33[31mA frase digitada não é um palíndromo!')