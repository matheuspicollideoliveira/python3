print('{:=^40}'.format('\33[1:32mLOJAS PICOLLI\33[m'))
valor = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print(30 * '-')
condicao = int(input('Qual a sua opção:'))
if condicao == 1:
    print(f'O preço do produto saíra com 10% de desconto e será de R${(valor * 0.9):.2f}!')
elif condicao == 2:
    print(f'O preço do produto saíra com 5% de desconto e será de R${(valor * 0.95):.2f}!')
elif condicao == 3:
    parcela = valor / 2
    print(f'Sua compra será pacelada em 2X de R${parcela:.2f} e o preço do produto será o mesmo, portanto R${(valor):.2f}!')
elif condicao == 4:
    parcela = int(input('Quantas parcelas?'))
    preco = valor * 1.2 / parcela
    print(f'Sua compra será parcelada em {parcela}X de R${preco:.2f}, o preço final do produto\nsaíra com 20% de juros e será de R${(valor * 1.2):.2f}')
else:
    print('\33[1:31mOPÇÃO INVÁLIDA DE PAGAMENTO! TENTE NOVAMENTE!')