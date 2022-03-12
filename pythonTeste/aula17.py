'''num = [0, 3, 9, 4]
num[2] = 8  # Troca o '9' pelo '8'
print(num)
# num[4] = 1 XXX # Não é possível adicionar valores dessa forma! Use num.insert() ou num.append()
num.append(1)   # Adiciona o '1' na última posição.
print(num)
num.insert(3, 1)   # Adiciona o '5' na posição '2' e empurra o restante para as posições adjacentes
print(num)
#num.pop()   # Remove o último argumento da variável
#num.pop(2)   # Remove o argumento na posição 2
num.remove(1)   # Remove o '1' somente na primeira ocorrência
print(num)
num.sort()   # Coloca em ordem do menor para o maior (numérica ou alfabética)
print(num)
num.sort(reverse=True) #  Coloca em ordem do maior para o menor
print(num)
if 7 in num:
    num.remove(7)
else:
    print('Não há número 7.')
print(f'Essa lista tem {len(num)} elementos.')'''

# Criando lista vazia:
valores = []  # Ou valores = list()
''''# Adicionando itens:
valores.append(4)
valores.append(9)
valores.append(5)
for v in valores:
    print(f'{v}...')'''

''''# Adicionando argumentos numa variável vazia através de input:
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# Identificando posições:
for c, v in enumerate(valores):
    print(f'Na posição {c} temos o elemento {v}.')'''

# Igualando listas:
a = [0, 3, 5, 9, 6]
# b = a
# b[2] = 2  # Não altera somente a lista 'b', mas também a lista 'a', pois é criada uma ligação entre elas.

# Criando uma cópia:
b = a[:]  # Recebe todos os ites da lista 'a', mas apenas como cópia (lista nova). As listas não têm ligação.
b[2] = 2
print(f'{a}')
print(f'{b}')  # Como foi criada um CÓPIA (lista nova), somente a lista b recebe a alteração.

### print(*num, sep= ', ')# '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista
#Exemplo:
names = ["Sam", "Peter", "James", "Julian", "Ann"]
print(*names, sep=", ")
#output: Sam, Peter, James, Julian, Ann