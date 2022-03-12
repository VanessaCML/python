n = []
'''for v in range(0, 5):
    n.append(int(input(f'Digite um número na posição {v}: ')))
print(f'Você digitou os números: ', end='')
print(*n, sep=', ')
print(f'O maior número é o {max(n)} na posição {n.index(max(n))} e o menor é {min(n)} na posição '
      f'{n.index(min(n))}.')'''

# sem usar o max() e min() & index():
ma = 0
me = 0
for v in range(0, 5):
    n.append(int(input(f'Digite um número na posição {v}: ')))
    if v == 0:
        ma = me = n[v]
    else:
        if n[v] > ma:
            ma = n[v]
        if n[v] < me:
            n[v] = me
print(f'O maior número é o {ma} na posição ', end='')
for pos, c in enumerate(n):
    if c == ma:
        print(f'{pos}...', end='')
print()
print(f'O menor número é o {me} na posição ', end='')
for pos, c in enumerate(n):
    if c == me:
        print(f'{pos}...', end='')



'''lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')'''




