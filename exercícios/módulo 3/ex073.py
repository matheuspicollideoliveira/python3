classificacao = ('Corinthians','Santos','Avaí','América-MG',
                 'Bragantino','Atlético-MG','São Paulo','Botafogo'
                 ,'Internacional','Coritiba','Cuibá','Athletico-PR'
                 ,'Palmeiras','Flamengo','Fluminense','Goiás'
                 ,'Ceará','Juventude','Atlético Goianiense','Fortaleza')
print(20 * '-=')
print(f'Lista de times do Brasileirão 2022: {classificacao}')
print(20 * '-=')
print(f'Os 5 primeiros times são {classificacao[0:5]}')
print(20 * '-=')
print(f'Os últimos 4 são {classificacao[-4:]}')
print(20 * '-=')
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print(20 * '-=')
print('O \33[1:32mPalmeiras\33[m está na {}ª posição!'.format(classificacao.index('Palmeiras')+1))
