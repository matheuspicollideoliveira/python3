def ficha(nome="<desconhecido>", g=0):
    """
    Mostrar o nome e a quantidade de gols de um jogador no campeonato.
    :param nome: Nome do Jogador
    :param gols: número de gols
    :return: nome e número de gols
    """
    print(f'O jogador {nome} fez {g} gol(s) no campeonato.')


print(45 * '-')
nome = str(input('Nome do jogador:'))
gols = str(input('Número de gols:'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

