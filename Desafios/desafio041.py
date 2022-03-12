from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
i = date.today().year - ano
if i < 5:
    print('\nCrianças abaixo de 5 anos não podem competir.')
elif i > 100:
    print('\nPessoas acima de 100 anos não podem competir.')
else:
    if 5 <= i <= 9:
        print(f'\nO atleta tem {i} anos. Categoria MIRIM.')
    elif i <= 14:
        print(f'\nO atleta tem {i} anos. Categoria INFANTIL.')
    elif i <= 19:
        print(f'\nO atleta tem {i} anos. Categoria JUNIOR.')
    elif i <= 25:
        print(f'\nO atleta tem {i} anos. Categoria SÊNIOR.')
    else:
        print(f'\nO atleta tem {i} anos. Categoria MASTER.')



'''from datetime import date
nasc = int(input('Digite o ano de nascimento do aluno: ').strip())
idade = date.today().year - nasc

#CATEGORIAS
mirim = range(0, 10)
infatil = range(10, 15)
junior = range(15, 20)
senior = range(20, 26)

#CONDIÇÕES
if idade in mirim:
    print('MIRIM. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in infatil:
    print('INFANTIL. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in junior:
    print('JUNIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade == senior:
    print('SENIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
else:
    print('MASTER. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))'''
