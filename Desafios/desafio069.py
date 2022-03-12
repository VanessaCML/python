print('-'*10)
print('CADASTRAMENTO')
print('-'*10)
maioridade = homem = mulhermenor20 = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    o = ' '
    while s not in 'FM':
        s = str(input('Sexo: ')).strip().upper()[0]
    if i >= 18:
        maioridade += 1
    if s in 'M':
        homem += 1
    if i < 20 and s in 'F':
        mulhermenor20 += 1
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if o == 'N':
        break
if maioridade > 1:
    print(f'Há {maioridade} pessoas acima de 18 anos.')
elif maioridade == 1:
    print(f'Há apenas {maioridade} pessoa maior de 18 anos.')
else:
    print(f'Não há pessoas maiores de 18 anos.')
if homem > 1:
    print(f'Há {homem} pessoas do sexo masculino.')
elif homem == 1:
    print(f'Há apenas {homem} pessoa do sexo masculino.')
else:
    print(f'Não há pessoas do sexo masculino.')
if mulhermenor20 > 1:
    print(f'Há {mulhermenor20} pessoas do sexo feminino abaixo de 20 anos.')
elif mulhermenor20 == 1:
    print(f'Há apenas {mulhermenor20} pessoa do sexo feminino abaixo de 20 anos.')
else:
    print(f'Não há pessoas do sexo feminino abaixo de 20 anos.')
