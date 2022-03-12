r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
lista = [r1, r2, r3]
ordem = sorted(lista)
if ordem[0] + ordem[1] <= ordem[2]:
    print('\nNão é possível formar um triângulo com essas 3 retas.')
else:
    if ordem[0] == ordem[1] == ordem[2]:
        print(f'\nAs retas {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo equilátero.')
    elif ordem[0] != ordem[1] != ordem[2]:
        print(f'\nAs retas {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo escaleno.')
    elif ordem [0] == ordem[1] or ordem [1] == ordem[2]:
        print(f'\nAs retas {r1:.2f}, {r2:.2f} e {r3:.2f} formam um triângulo isósceles.')
