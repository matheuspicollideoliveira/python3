jogador = dict()
gols = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador?'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['gols'] = gols[:]
for v in gols:
    tot += v
#ou jogador['total'] = sum(gols)
jogador['total'] = tot
print(30 * '-=')
print(jogador)
print(30 * '=-')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(30 * '=-')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'  => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
