numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite  o {c}° número: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')