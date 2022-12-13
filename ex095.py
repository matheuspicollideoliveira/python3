plantel = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador?'))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    plantel.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if r in 'SN':
            break
        print('Erro. Digite apenas S ou N!')
    print(30 * '-')
    if r in 'N':
        break
print(30 * '-=')
print('cod', end='   ')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print(40 * '-')
for i, e in enumerate(plantel):
    print(f'{i:<3}', end='   ')
    for v in e.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(plantel):
        print(f'Erro. Não existe jogador com o código {busca}!')
    if busca < len(plantel):
        print(f'--LEVANTAMENTO DO JOGADOR {plantel[busca]["nome"]}:')
        for i, g in enumerate(plantel[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('Volte sempre!!!')
