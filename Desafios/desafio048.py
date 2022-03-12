soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print(f'A soma dos {cont} números é {soma}.')
