from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = False
while not menu:
    o = int(input(f'\n[1] SOMAR'
                  f'\n[2] MULTIPLICAR'
                  f'\n[3] MAIOR'
                  f'\n[4] NOVOS NÚMEROS'
                  f'\n[5] SAIR DO PROGRAMA'
                  f'\n>>>>> Qual sua opção: '))
    if 1 > o or o > 5:
        print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE EM ALGUNS INSTANTES.')
    else:
        if o == 5:
            print('\nFinalizando...')
            menu = True
        else:
            if o == 1:
                print(f'\nO resultado da soma entre {n1} e {n2} é {n1+n2}.')
            elif o == 2:
                print(f'\nO resultado da multiplicação entre {n1} e {n2} é {n1*n2}.')
            elif o == 3:
                lista = [n1, n2]
                a = sorted(lista)
                if n1 != n2:
                    print(f'\nO maior número é {a[1]}.')
                else:
                    print(f'\nOs números são iguais.')
            if o == 4:
                n1 = int(input('\nDigite um número: '))
                n2 = int(input('Digite outro número: '))
    print('\n', '=+=' * 20)
    sleep(2)
print('\nFIM DO PROGRAMA')
