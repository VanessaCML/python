def fatorial(num, show=False):
    """
    Cálculo de fatorial
    :param num: Número a ser calculado
    :param show: Exibe ou não o cálculo do fatorial
    :return: O valor do fatorial de um número "num"
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ' if c > 1 else f'{c} = ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)