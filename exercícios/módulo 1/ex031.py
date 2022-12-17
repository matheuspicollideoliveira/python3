d = int(input('Digite a distância da sua viagem em Km:'))
dl = d * 0.45
dc = d * 0.5
if d > 200:
    print(f'Sua viagem irá custar R${int(dl):.2f}!')
else:
    print(f'Sua viagem irá custar R${(dc):.2f}!')

#ou

d = int(input('Digite a distância da sua viagem em Km:'))
preço = d * 0.50 if d < 200 else d * 0.45
print(f'O preço da sua viagem é {preço}')

