print('\33[1;33m~*\33[m'*20)
print(f'\33[1;33m{"LISTA DE PREÇOS":^40}\33[m')
print('\33[1;33m~*\33[m'*20)
lista = 'Monitor', 1200, 'Placa de vídeo', 3900, \
        'Teclado mecânico', 380, 'Mouse', 120, \
        'Processador', 1500, 'HD 1T', 530, \
        'Memória RAM', 350, 'CPU', 1500
for c in range(0, 14, 2):
    print(f'\33[37m{lista[c]:.<32}\33[m', f'\33[32mR$ {lista[c+1]:>4}\33[m')
print('\33[1;33m~*\33[m'*20)


'''for i in lista:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')'''