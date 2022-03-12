times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athlético-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport', 'Chapecoense')
for pos, c in enumerate(times[:4]):
    print(f'O {pos+1}° colocado no Campeonato Brasileiro de 2021 foi o {c}.')
'\n'
for pos, c in enumerate(times[-4:]):
    print(f'O {pos+17}° colocado no Campeonato Brasileiro de 2021 foi o {c}.')
print(f'\nOs times em ordem alfabética: ')
print(sorted(times))
posi = times.index('Chapecoense')+1
print(f'O chapecoense está na posição {posi}.')


# for t in times:
#     print(t)
