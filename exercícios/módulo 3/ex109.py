import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,False)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% do valor temos {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13% do valor temos R${moeda.diminuir(p,13,True)}')