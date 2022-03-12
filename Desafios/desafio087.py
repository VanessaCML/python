matriz = [[], [], []]
somapar = somacol = ma = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um número na posição {l, c}: '))
        if c == 0:
            matriz[l].append(n)
        elif c == 1:
            matriz[l].append(n)
        else:
            matriz[l].append(n)
        if n % 2 == 0:
            somapar += n
        if c == 2:
            somacol += n
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='  ')
    print()
print(f'A soma dos números pares é {somapar}.')
print(f'A soma da coluna 3 é {somacol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > ma:
        ma = matriz[1][c]
print(f'O maior número da linha 2 é {ma}.')


# Outra forma de resolver as somas: (abaixo do primeiro print, usando a variável 'matriz[l][c]')
'''for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
            
for l in range(0, 3):
    somacol += matriz[l][2]'''


