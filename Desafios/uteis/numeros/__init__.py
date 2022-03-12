def fatorial(num):
    f = 1
    for c in range(1, num + 1):
        f *= c
    return f


def dobro(num):                  # TODAS ESSAS FUNÇÕES PODEM SER COLOCADAS EM UM ARQUIVO NOVO, PARA ORGANIZAÇÃO E PARA
    return num * 2               # QUE O PROGRAMA NÃO FIQUE ENORME E SEJA FÁCIL ACESSAR AS FUNÇÕES QUANDO PRECISO,
                                 # DESSA FORMA, SÓ FICA O CÓDIGO PRINCIPAL DENTRO DO PROGRAMA.

def triplo(num):
    return num * 3
