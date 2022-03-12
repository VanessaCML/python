lista = 'moto', 'cadeira', 'amanhecer', 'dedicar', 'programa', \
        'descer', 'devagar', 'cozinhar', 'batata', 'menina', \
        'celular', 'atacar', 'banana', 'remedio', 'roldana', 'grndr'
for p in lista: # Analisa e roda cada palavra da lista
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for l in p: # Analisa cada letra da palavra escolhida no for acima
        if l.lower() in 'aeiou':
            print(l, end=' ')
