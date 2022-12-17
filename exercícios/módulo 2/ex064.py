tot = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]:'))
    if n != 999:
        tot += n
        cont += 1
print(f'Você digitou {cont} números é a soma entre eles foi {tot}!')