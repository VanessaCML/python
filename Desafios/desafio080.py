n = []
for c in range(0, 5):
    a = int(input('Digite um número: '))
    if c == 0 or a > n[-1]:
        n.append(a)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(n):
            if a <= n[pos]:
                n.insert(pos, a)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print(f'Você digitou os números {n}.')
