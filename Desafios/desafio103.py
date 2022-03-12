def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


j = str(input('Digite o nome do jogador: ')).title().strip()
g = str(input('Digite o número de gols: '))
if g.isnumeric():
    int(g)
else:
    g = 0
if j == '':
    ficha(gol=g)
else:
    ficha(j, g)

