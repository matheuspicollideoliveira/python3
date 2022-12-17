ficha = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
print(30 * '=-')
print('{:<4}{:<10}{:>8}'.format('No.', 'NOME', 'MÉDIA'))
print(26 * '-')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print(35 * '-')
while True:
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe]'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        print(35 * '-')
print('Volte sempre!')







