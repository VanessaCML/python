lista = []
c = 0
while True:
    n = int(input('Digite um número: '))
    if c == 0 or n < lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n >= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
    c += 1
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print(f'Os números digitados foram {lista}.')
print(f'Foram digitados {len(lista)} números.')
if 5 in lista:
    print('O número 5 está contido na lista.')
else:
    print('O número 5 não está na lista.')
