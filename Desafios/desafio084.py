pessoas = []
dados = []
ma = me = 0
nomemenor = nomemaior = ''
while True:
    n = str(input('Nome: ')).strip().title()
    while n.isalpha() == False:
        n = str(input('Caractere inválido. Tente novamente. Nome: '))
    dados.append(n)
    pe = float(input('Peso: '))
    dados.append(pe)
    if len(pessoas) == 0: # ou if not pessoas:
        ma = me = dados[1]
    else:
        if dados[1] > ma:
            ma = dados[1]
        if dados[1] < me:
            me = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print(pessoas)
print(f'Você cadastrou {len(pessoas)} pessoas no total.')
print(f'Maior peso {ma} de: ', end='')
for p in pessoas:
    if p[1] == ma:
        print(f'{[p[0]]} ', end='')
print(f'\nMenor peso {me} de: ', end='')
for p in pessoas:
    if p[1] == me:
        print(f'{[p[0]]} ', end='')
print()


#Outra forma de resolver, criando lista para os mais leves e mais pesados.
'''cadastro = list()
pesados = list()
leves = list()
while True:
    n = str(input('Nome: ').strip().capitalize())
    i = float(input('Peso: ').strip())
    cadastro.append([n, i])
    mais = str(input('Cadastrar outra pessoa? [S/N] ').strip())
    if mais in "Nn":
        break
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas.')
maior = 0
for pessoa in cadastro:
    if pessoa == 0:
        maior = pessoa[1]
        pesados.append(pessoa)  # Aqui ele vai guardar ('nome', peso) na lista 'pesados'.
    else:
        if pessoa[1] > maior:
            pesados.clear()
            maior = pessoa[1]
            pesados.append(pessoa)
        elif pessoa[1] == maior:
            pesados.append(pessoa)
print(f'O maior peso foi {maior} kg. Peso de: ', end='')
for c in pesados:
    print('', c[0], end='')
print()
menor = maior
for pessoa in cadastro:
    if pessoa == 0:
        menor = pessoa[1]
        leves.append(pessoa)
    else:
        if menor > pessoa[1]:
            leves.clear()
            menor = pessoa[1]
            leves.append(pessoa)
        elif pessoa[1] == menor:
            leves.append(pessoa)
print(f'O menor peso foi de {menor} kg. Peso de:', end='')
for c in leves:
    print('', c[0], end='')'''