from desafio111.utilidadeCeV import dado
import CORES

def linha(tam=42):
    return '=' * tam


def cab(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cab('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[36m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    r = dado.leiaInt('\033[32mDigite sua opção: \033[m')
    return r
