'''n = int(input('Digite um número: '))
cont = n
f = 1
while cont > 0:
    print(f'{cont}', end='')
    print(f' x 'if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f'{f}.')'''


'''fat = int(input('Digite um número: '))
for c in range(fat - 1, 0, -1):
    fat = fat * c
print('O fatorial desse número é {fat}.')'''


'''n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for n1 in range(n1, 0, -1):
    acumulador *= n1
print('O produto de todos os números é {}'.format(acumulador))'''


n = int(input('Digite um número: '))
cont = n
f = 1
for c in range(n, 0, -1):
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f'{f}')

# Consegui refazer sozinha depois:
n = int(input('Digite um número: '))
c = n
fat = 1
while c > 0:
    fat *= c
    print(f'{c} x ' if c > 1 else f'{c} = ', end='')
    c -= 1
print(fat)

n = int(input('Digite um número: '))
c = n
fat = 1
for c in range(c, 0, -1):
    fat *= c
    print(f'{c} x ' if c > 1 else f'{c} = ', end='')
    c -= 1
print(fat)

