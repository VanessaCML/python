infojogador = {}
gols = []
infojogador['nome'] = str(input('Nome do jogador: ')).strip().title()
n = int(input(f'Quantas partidas {infojogador["nome"]} jogou: '))
for partida in range(0, n):
    gols.append(int(input(f'Quantos gols na partida {partida+1}: ')))
infojogador['gols'] = gols[:]
infojogador['total'] = sum(gols)
print('~'*50)
print(infojogador)
print('~'*50)
for k, v in infojogador.items():
    print(f'O campo {k.upper()} tem valor {v}.')
print('~'*50)
print(f'O jogador {infojogador["nome"]} jogou {n} partidas.') #Ou len(infojogador["gols"])
for i, v in enumerate(infojogador['gols']):
    print(f'===>Na partida {i+1} fez {v} gol(s).')
print(f'Foi um total de {infojogador["total"]} gol(s).')
print('~'*50)
