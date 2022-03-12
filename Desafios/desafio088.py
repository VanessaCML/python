from random import randint
from time import sleep
sorteio = []
c = 0
n = int(input('Quantos jogos você quer que eu sorteie: '))
for b in range(0, n):
    b = list()
    sorteio.append(b)
    while len(b) != 6:
        jogo = randint(1, 60)
        if jogo not in b:
            b.append(jogo)
for i, s in enumerate(sorteio):  # O 'i' mostra a posição e o 's' mostra o conteúdo daquela posição
    sorteio[i].sort()
    print(f'Jogo {i+1}: {s}')
    sleep(1)
# OU:
'''for s in range(0, len(sorteio)):
    sorteio[s].sort()
    print(f'Jogo {s+1}: {sorteio[s]}')
    sleep(1)'''
