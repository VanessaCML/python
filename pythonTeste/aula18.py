'''teste = list()
teste.append('Ana')
teste.append(25)

galera = list()
#galera.append(teste) # A lista "teste" fica dentro da lista "galera"
galera.append(teste[:]) # Cria uma cópia da lista "teste" e não será alterada com os comandos de baixo

teste[0] = 'Maria'
teste[1] = 37

galera.append(teste[:]) # Cria a cópia da lista "teste" logo após a alteração dos comandos acima
# Logo as duas listas ficam independentes e somente a lista-base "teste" é alterada.
print(galera)'''

'''galera = [['Rosa', 27], ['José', 77], ['Amanda', 19], ['Luis', 37]]
# print(galera[0]) -> ['Rosa', 27]
# print(galera[2][0])  # -> Amanda

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')
    #print(*p, sep=", ")'''


galera = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) #caso eu não faça a cópia com "[:]", ele apagaria tudo da lista "galera" também.
    dados.clear()
#print(galera)

totmaior = totmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Há {totmaior} pessoa(s) maior de idade e {totmenor} menor de idade.')