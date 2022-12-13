from datetime import date
a = int(input('Digite um ano qualquer ou digite 0 para saber se o ano atual é bissexto:'))
if a == 0:
    a = date.today().year
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(f'O ano de {a} é bissexto!')
else:
    print(f'O ano de {a} não é bissexto!')