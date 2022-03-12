import CORES


def leiaDinheiro(msg):
    a = str(input(msg)).strip()
    while a.isalpha() or a == '':
        print(f'"{a}" é uma entrada inválida.')
        a = str(input(msg)).strip()
    a = float(a.replace(',', '.'))
    return a


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro. Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = (input(msg))
            while True:
                n = float(n.replace(',', '.'))
                break
        except (TypeError, ValueError):
            print('\033[31mErro. Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mPrograma interrompido pelo usuário.\033[m')
            return 0
        else:
            return n


