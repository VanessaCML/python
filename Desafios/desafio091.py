from random import randint
from time import sleep
from operator import itemgetter

'''jogo = {}
for j in range(0, 4):
    a = randint(1, 6)
    print(f'Jogador {j+1} jogou {a}')
    temp = {f'Jogador {j + 1}': f'{a}'}                
    sleep(1)
print(jogo)'''



jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
print('RANKING')
for pos, r in enumerate(ranking):
    print(f'Em {pos + 1}° lugar: {r[0]} com {r[1]}')
