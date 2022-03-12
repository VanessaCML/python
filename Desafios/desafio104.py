def leiaInt(num):
    n = str(input(num))
    while n == '' or not n.isnumeric():
        print('\033[31mErro! Você não digitou um número válido.\033[m')
        n = str(input(num))
    return n


n = leiaInt('Digite um número: ')
print(f'\033[32mVocê digitou o número {n}.\033[m')


# Resolução do professor:
'''def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = int(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Você não digitou um número válido.\033[m')
        if ok:
            break
    return valor'''
