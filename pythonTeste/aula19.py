'''pessoas = {'nome': 'Vanessa', 'sexo': 'F', 'idade': 32}
pessoas['peso'] = 55.6
print(pessoas)
print()
print(pessoas['nome'])
print()
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)  # Mostra: nome sexo idade
print()
for k in pessoas.values():
    print(k)  # Mostra: Vanessa F 32
print()
for k in pessoas.items():
    print(k)  # Mostra ('nome', 'Vanessa') ('sexo', 'F') ('idade', 32)
print()
pessoas['nome'] = 'Ana' # Como alterar as chaves
for k, v in pessoas.items(): #k é keys, v é valores
    print(f'{k.title()} é {v}.')
#del pessoas['sexo'] # Apaga a chave e o valor (sexo e F)'''

#CRIANDO DICIONÁRIO DENTRO DE UMA LISTA:
'''brasil = [] # OU brasil = dict()
estado1 = {'uf': 'Bahia', 'sigla': 'BA'}
estado2 = {'uf': 'Alagoas', 'sigla': 'AL'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Estado: ')).strip()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()
    brasil.append(estado.copy())
for e in brasil:
    '''for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')'''
    for v in e.values():
        print(v, end=' ')
    print()








