def ajuda(msg):
    n = ' '
    from time import sleep
    while n not in 'fim':
        print('\033[1;97;45m<>' * 20)
        print(f'{"MANUAL PyHELP":^38}')
        print('<>' * 20)
        print('\033[m', end='')
        n = str(input('Digite uma função ou biblioteca: ')).strip().lower()
        if n == 'fim':
            sleep(2)
            print('\033[1;97;41m<>' * 20)
            print(f'{"FIM DO TUTORIAL":^38}')
            print('<>' * 20)
            print('\033[m')
            break
        print('\033[1;97;43m~' * 40)
        print(f'{"Acessando o manual...AGUARDE":^38}')
        print('~' * 40)
        print('\033[m', end='')
        sleep(2)
        print('\033[7;97;40m')
        help(n)
        print('\033[m', end='')
        sleep(2)

resp = ' '
ajuda(resp)
