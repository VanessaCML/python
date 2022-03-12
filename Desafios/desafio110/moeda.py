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


def titulo(txt):
    t = len(txt)
    print('~' * t)
    print(f'{txt}')
    print('~' * t)


def resumo(n=0, tx1=0, tx2=0):
    a = aumentar(n, tx1)
    d = diminuir(n, tx2)
    m = metade(n)
    db = dobro(n)
    titulo(f'{"DADOS DO VALOR"}'.center(30))
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(db)}')
    print(f'Metade do preço: \t{moeda(m)}')
    print(f'{tx1}% de aumento: \t{moeda(a)}')
    print(f'{tx2}% de desconto: \t{moeda(d)}')
    titulo(f'{"FIM"}'.center(30))


