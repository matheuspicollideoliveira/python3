cidade = str(input('Digite o nome da sua cidade:')).strip()
divido = cidade.upper().split()
print('\33[1:34mO nome da cidade começa com a palavra "Santo"?\33[m')
print('SANTO' in divido[0])

#ou

cidade = str(input('Digite o nome da sua cidade:')).strip()
print(cidade[:5].upper() == 'SANTO')