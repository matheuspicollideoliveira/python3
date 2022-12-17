def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado!
    :param show:(opcional) Mostra ou não a conta.
    :return:O valor do fatorial de um número n
    """
    print(30 * '-')
    print(f'Calculando o fatorial de {n}!:')
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c
    return f


print(fatorial(5))
print(fatorial(6, True))





