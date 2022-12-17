n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média é {media} e você está REPROVADO!')
elif 5 <= media <= 6.9:
    print(f'Sua média é {media} e você está de recuperação!')
else:
    print(f'Sua média é {media} e você está APROVADO!')