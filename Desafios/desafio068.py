from random import randint
c = 0
jogador = int(input('Escolha um número entre 0 e 10: '))
while True:
    while jogador not in (0, 10):
        jogador = int(input('Escolha um número entre 0 e 10: '))
        print('=-=' * 20)
    pc = randint(0, 10)
    total = jogador + pc
    o = ' '
    while o not in 'PI':
        o = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
        print('=-=' * 20)
    if total % 2 == 0:
        if o in 'Pp':
            print(f'{total} é PAR! VOCÊ GANHOU! Você jogou {jogador} e o eu {pc}. '
                  f'Vamos jogar novamente...')
            print('=-='*20)
        else:
            print(f'{total} é PAR! VOCÊ PERDEU! Você jogou {jogador} e eu {pc}.')
            break
    else:
        if o in 'Ii':
            print(f'{total} é ÍMPAR! VOCÊ GANHOU! Você jogou {jogador} e o eu {pc}. '
                  f'Vamos jogar novamente...')
            print('=-=' * 20)
        else:
            print(f'{total} é ÍMPAR! VOCÊ PERDEU! Você jogou {jogador} e eu {pc}.')
            break
    c += 1
print('=-='*20)
print(f'Você ganhou {c} vez(es) consecutiva(s).')
print('=-='*20)
