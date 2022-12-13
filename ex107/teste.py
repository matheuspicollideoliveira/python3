import moeda107

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda107.metade(p)}')
print(f'O dobro de R${p} é R${moeda107.dobro(p)}')
print(f'Aumentando 10% do valor temos R${moeda107.aumentar(p,10)}')
print(f'Diminuindo 13% do valor temos R${moeda107.diminuir(p,13)}')