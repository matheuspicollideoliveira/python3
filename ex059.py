from time import sleep
n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
print(40 * '-')
escolha = 0
while escolha != 5:
    print('''MENU:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior 
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
    escolha = int(input('>>>>Digite sua opção:'))
    if escolha == 1:
        print(f'\33[32mA soma entre {n1} + {n2} é {n1 + n2}\33[m!')
        print(15 * '-==')
    elif escolha == 2:
        print(f'\33[33mO resultado de {n1} x {n2} é {(n1 * n2):.2f}\33[m!')
        print(15 * '-==')
    elif escolha == 3:
        if n1 > n2:
            print(f'\33[34mEntre {n1} e {n2} o maior valor é {n1}!\33[m')
            print(15 * '-==')
        elif n2 > n1:
            print(f'\33[34mEntre {n1} e {n2} o maior valor é {n2}!\33[m')
            print(15 * '-==')
        elif n1 == n2:
            print(f'\33[34mOs valores são iguais!\33[m')
            print(15 * '-==')
    elif escolha == 4:
        print('Informe os novos números:')
        n1 = int(input('Digite o 1º número:'))
        n2 = int(input('Digite o 2º número:'))
    elif escolha == 5:
        print('\33[37mFinalizando...\33[m')
        sleep(1)
    else:
        print('\33[1:31mOpção inválida, tente novamente!\33[m')
        print(15 * '-==')
print('\33[35mObrigado por utilizar nosso programa!!!')