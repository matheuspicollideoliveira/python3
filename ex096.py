def area(l, c):
    print(f'A área de um terreno de {l} x {c} é de {l*c}m²')


print(30 * '-')
print('{:^30}'.format('CONTROLE DE TERRENOS'))
print(30 * '-')
area(l=float(input('LARGURA (m):')), c=float(input('COMPRIMENTO (m):')))
