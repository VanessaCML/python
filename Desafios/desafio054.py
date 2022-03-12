from datetime import date
contma = 0
contme = 0
atual = date.today().year
for n in range(1, 8):
    ano = int(input(f'Qual o ano de nascimento da {n}° pessoa: '))
    if atual - ano >= 21:
        contma += 1
    else:
        contme += 1
print(f'Há {contma} pessoas maiores de idade e {contme} menores de idade.')
