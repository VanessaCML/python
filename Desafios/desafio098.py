from time import sleep


def contador(i, f, p):
    while True:
        if p == 0:
            p += 1
        if p != 0:
            print('<>'*15)
            print(f'Contagem de {i} a {f} de {p} em {p}')
            if i < f:
                for c in range(i, f + 1, p):
                    print(f'{c:^2}', end=' ')
                    #sleep(0.3)
            else:
                for c in range(i, f - 1, -p):
                    print(f'{c:^2}', end=' ')
                    #sleep(0.3)
        break


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('<>'*15)
i = int(input('Número inicial: '))
f = int(input('Número final: '))
p = abs(int(input('Passo: ')))  # Pega o número inteiro, sem sinal (positivo)
contador(i, f, p)
print()
print('<>'*15)
