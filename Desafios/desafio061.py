n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0
t = n
while cont < 10:
    print(f'{t} -> 'if cont < 9 else f'{t}', end='')
    t += r
    cont += 1
