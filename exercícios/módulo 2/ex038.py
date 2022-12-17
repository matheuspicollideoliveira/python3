n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite um número inteiro:'))
if n1 > n2:
    print(f'\33[35mO número {n1} é maior do que o número {n2}!')
elif n2 > n1:
    print(f'\33[36mO número {n2} é maior do que o número {n1}!')
else:
    print('\33[32mNão existe valor maior, os números são iguais!')