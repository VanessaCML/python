def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos. \nVoto NEGADO.'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos. \nVoto FACULTATIVO'
    if 18 < idade < 65:
        return f'Com {idade} anos. \nVoto OBRIGATÓRIO'


n = int(input('Ano de nascimento: '))
print(voto(n))
