'''f = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(f)
comp = len(junto)
inv = ''
for l in range(comp-1, -1, -1):
    inv += junto[l]
print(f'O inverso de {junto} é {inv}.')
if junto == inv:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')'''


f = str(input('Digite uma frase: ')).upper().strip().split()
junto = ''.join(f)
comp = len(junto)
inv = junto[::-1]
print(f'O inverso de {junto} é {inv}.')
if junto == inv:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
