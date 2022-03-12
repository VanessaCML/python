def fatorial(num):
    f = 1
    for c in range(1, num + 1):
        f *= c
    return f


n = int(input('Digite um número: '))
fat = fatorial(n)
print(f'O fatorial de {n} é {fat}.')
