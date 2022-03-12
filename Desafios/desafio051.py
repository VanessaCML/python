n = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão: '))
d = n + (10 - 1) * r
for c in range(n, d + r, r):
    print(f'{c} -> ', end='')
print('FIM')
