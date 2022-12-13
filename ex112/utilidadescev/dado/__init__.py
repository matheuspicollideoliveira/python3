def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\33[31mERRO: \"{n}\" é um preço inválido.\33[m')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return valor


def resumo(n=0, a=10, d=5):
    print(30 * '-')
    print('RESUMO DO VALOR'.center(30))
    print(30 * '-')
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'{a}% de aumento: \t{aumentar(n,a,True)}')
    print(f'{d}% de redução: \t{diminuir(n,d,True)}')
    print(30 * '-')