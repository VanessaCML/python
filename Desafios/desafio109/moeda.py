def aumentar(n=0, tx=0, formato=False):
    aum = n + (n * tx / 100)
    if formato:
        return moeda(aum)
    else:
        return aum


def diminuir(n=0, tx=0, formato=False):
    dim = n - (n * tx / 100)
    return dim if formato is False else moeda(dim)


def metade(n=0, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)


def dobro(n=0, formato=False):
    dob = n * 2
    return dob if formato is False else moeda(dob)


def moeda(n=0, m='R$ '):
    return f'{m}{n:.2f}'.replace('.', ',')
