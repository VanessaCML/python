cadastro = []
somaidade = 0
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Erro! Por favor, tente novamente. Sexo[M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    somaidade += pessoa['idade']
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print('~' * 50)
print(cadastro)
print('~' * 50)
print(f'O grupo tem {len(cadastro)} pessoas.')
media = somaidade / len(cadastro)
print(f'A média de idade é {media:.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for c in range(0, len(cadastro)):
    if cadastro[c]['sexo'] == 'F':
        print(f'{cadastro[c]["nome"]}', end=' ')
print()
print('Lista das pessoas acima da média:')
for c in cadastro:
    if c['idade'] > media:
        for k, v in c.items():
            print(f'{k.title()} = {v};', end= ' ')
        print()
