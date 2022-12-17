n = tot = cont = 0
while True:
    n = float(input('Digite um valor [999 para parar]:'))
    if n == 999:
        break
    tot += n
    cont += 1
print(f'A soma dos {cont} valores é {tot}!')
