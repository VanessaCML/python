c = 0
soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma = (soma + n)
    c += 1
    n = int(input('Digite um número: '))
if c == 0:
    print('Você não digitou nenhum número.')
else:
    print(f'Foram digitados {c} números e a soma entre eles é {soma}.')
