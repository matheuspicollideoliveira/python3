def leiaInt(msg):
    """
    Retorna um valor caso ele seja um número inteiro!
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[31mErro. Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')

