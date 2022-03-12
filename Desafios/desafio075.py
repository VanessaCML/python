n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
# ou n = tuple(int(input('Digite um número: '))for c in range(1, 5))
print(f'Você digitou os números: {n}')
print(f'O número 9 apareceu {n.count(9)} vez(es).')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}a posição.')
else:
    print('O número 3 não apareceu.')
print('Os números pares digitados são: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
    else:
        print('nenhum')
    break
