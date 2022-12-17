from datetime import date
ano = int(input('Digite o ano que você nasceu:'))
print('''Digite seu sexo, sendo:
[ m ] Masculino
[ f ] Feminino''')
sexo = str(input('Sexo:')).lower()
idade = date.today().year - ano
if sexo == 'm':
    if idade < 18:
        print(f'Você está com {idade} anos em {date.today().year}e terá que se alistar ao serviço militar daqui {18 - idade} anos!\nSeu alistamento será em {ano + 18}!')
    elif idade == 18:
        print(f'Você está com {idade} anos em {date.today().year}, está na hora de se alistar ao serviço militar!')
    elif idade > 18:
        print(f'Você está com {idade} anos em {date.today().year}, já se passaram {idade - 18} anos do tempo de se alistar ao serviço militar!\nSeu alistamento foi em {ano + 18}!')
elif sexo == 'f':
    print('\33[31mVocê não precisa se alistar!\33[m')
else:
    print('\33[35mSexo indefinido!')