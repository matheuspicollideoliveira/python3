from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa:'))
    idade = date.today().year - ano
    if idade < 21:
        cont += 1
    elif idade >= 21:
        cont2 += 1
print(f'\33[1:35m{cont} pessoas são menores de idade\33[m e \33[1:36m{cont2} são maiores de idade!')

