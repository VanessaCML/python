from datetime import date
print('Qual seu sexo?'
      '\n1 para feminino'
      '\n2 para masculino')
s = int(input('\nInsira: '))
if s == 1:
    print('Pessoas do sexo feminino não precisam se alistar obrigatoriamente.')
else:
    ano = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano
    print(f'\nQuem nasceu em {ano} completa {idade} anos em 2022.')
    if idade < 18:
        if 18 - idade == 1:
            print(f'Falta {18 - idade} ano para o alistamento, '
            f'que deverá ser feito em {date.today().year + (18 - idade)}.')
        elif (18 - idade) > 1:
            print(f'Faltam {18 - idade} anos para o alistamento, '
                  f'que deverá ser feito em {date.today().year + (18 - idade)}.')
    elif idade == 18:
        print(f'O alistamento deverá ser feito neste ano.')
    else:
        if idade - 18 > 1:
            print(f'O período de alistamento foi há {idade - 18} anos no ano de {date.today().year - (idade - 18)}.')
        elif idade == 1:
            print(f'O período de alistamento foi há {idade - 18} ano no ano de {date.today().year - (idade - 18)}.')

