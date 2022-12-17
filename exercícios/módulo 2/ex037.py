num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases de conversão:')
print('[ 1 ] coverter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] coverter para HEXADECIMAL')
opção = int(input('Digite sua opção:'))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}!')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}!')
elif opção == 3:
    print(f'{num} convertido em HEXADECIMAL é igual a {hex(num)[2:]}!')
else:
    print('\33[31mOpção inválida. Tenet novamente!')
