n = []
while True:
    a = int(input('Digite um número: '))
    if a not in n:
        n.append(a)
    else:
        print('Número duplicado, não posso adicionar...')
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if o == 'N':
        break
n.sort()
print(f'Os valores digitados foram {n}')
