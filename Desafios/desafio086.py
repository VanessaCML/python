matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um número na posição {l, c}: '))
        if c == 0:
            matriz[l].append(n)
        elif c == 1:
            matriz[l].append(n)
        else:
            matriz[l].append(n)
for a in range(0, 3):
    for m in range(0, 3):
        print(f'[{matriz[a][m]:^7}]', end='  ' if m < 2 else '\n')


#Resolução do prof:
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número na posição {l, c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end=' ')
    print()'''

# Criar lista do tamanho que o usuário desejar:
'''matriz = []
for a in range(0, 4):   # 4 é o valor de 'n' que criei aqui
    a = []
    matriz.append(a)
print(matriz)'''