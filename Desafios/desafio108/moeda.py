def aumentar(n=0, tx=0, formato=False):
    aum = n + (n * tx / 100)
    return aum


def diminuir(n=0, tx=0, formato=False):
    dim = n - (n * tx / 100)
    return dim


def metade(n=0, formato=False):
    met = n / 2
    return met


def dobro(n=0, formato=False):
    dob = n * 2
    return dob


def moeda(n=0, m='R$ '):
    return f'{m}{n:.2f}'.replace('.', ',')



