s = c = b = barato = 0
barnome = ''
while True:
    n = str(input('Digite o nome do produto: ')).strip().title()
    p = float(input('Digite o preço do produto: R$ '))
    b += 1
    s += p
    if p >= 1000:
        c += 1
    if b == 1 or p < barato:
        barato = p
        barnome = n
    #else:
        #if p < barato:       Essas 4 linhas podem ser substituidas por 'or p < barato' pois as variaveis contidas
            #barato = p       nelas são iguais às de cima. SIMPLIFICAÇÃO!
            #barnome = n
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print(f'O total gasto é de R$ {s}.')
print(f'Há {c} produto(s) acima de R$ 1000.')
print(f'O produto mais barato é {barnome} que custa R$ {barato}.')
