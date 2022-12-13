def metade(n=0, s=False):
    if s:
        return f'R${n/2:.2f}'
    else:
        return n/2


def dobro(n=0, s=False):
    if s:
        return f'R${n * 2:.2f}'
    else:
        return n * 2

def aumentar(n, p, s=False):
    if s:
        return f'R${n * (1 + p/100):.2f}'
    else:
        return n * (1 + p/100)


def diminuir(n, p, s=False):
    if s:
        return f'R${n * (1 - p/100):.2f}'
    else:
        return n * (1 - p/100)


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, a, d):
    print(30 * '-')
    print('{:^30}'.format('RESUMO DO VALOR'))
    print(30 * '-')
    print('{:<20}'.format('Preço Analisado:'), end='')
    print(f'R${n:>7.2f}')
    print('{:<20}'.format('Metade do preço:'), end='')
    print(f'R${n / 2:>7.2f}')
    print('{:<20}'.format('Dobro do preço:'), end='')
    print(f'R${n * 2:>7.2f}')
    print('{:<20}'.format(f'{a}% de aumento:'), end='')
    print(f'R${n * (1 + a/100):>7.2f}')
    print('{:<20}'.format(f'{d}% de redução:'), end='')
    print(f'R${n * (1 - d/100):>7.2f}')
    print(30 * '-')


