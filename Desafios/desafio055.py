maior = 0
menor = 0
for pes in range(1, 6):
    p = float(input(f'Peso da {pes}° pessoa: '))
    if pes == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso é {maior} e o menor é {menor}.')


'''pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print('O maior peso é {}Kg' .format(max(pesos)))
print('O menor peso é {}Kg' .format(min(pesos)))'''