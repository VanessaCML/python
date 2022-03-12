from random import randint
lista = []


def sorteia():
    for c in range(0, 5):
        lista.append(randint(1, 100))
    print(f'A lista é formada pelos números {lista}')


def somapar():
    soma = 0
    for c in range(len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'A soma dos números pares de {lista} é {soma}.')

sorteia()
somapar()
