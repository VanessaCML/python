lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if o == 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa é {lista}.')
print(f'A lista de par é {par}.')
print(f'A lista ímpar é {impar}')
