from time import sleep


def contador(i, f, p):
    if i > f and p > 0:
        for c in range(i, f + p, p):
            sleep(0.5)
            print(c, end=' ')
    else:
        for c in range(i, f, p):
            sleep(0.5)
            print(c, end=' ')
    sleep(0.5)
    print('FIM')
    print(15 * '=-')


print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 11, 1)
print('Contagem de 10 até 0 de 2 em 2:')
contador(10, -2, -2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
print(15 * '=-')
if inicio > fim and passo > 0:
    passo = passo * -1
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    contador(inicio, fim + passo, passo)
else:
    if passo == 0:
        passo = passo + 1
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    contador(inicio, fim, passo)
