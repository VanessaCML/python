lista = []
alunos = []
nomes = []
notas = []
medias = []
m = 0
while True:
    while True:
        nome = str(input('Nome do aluno: ')).strip().title()
        while not nome.isalpha() and nome.isspace():
            nome = str(input('Caractere inválido. Digite novamente o nome do aluno: ')).strip().title()
        nomes.append(nome)
        notas.append(float(input('Digite a 1a nota: ')))
        notas.append(float(input('Digite a 2a nota: ')))
        m = (notas[0] + notas[1]) / 2
        medias.append(m)
        alunos.append(nome[:])
        alunos.append(notas[:])
        alunos.append(medias[:])
        nomes.clear()
        notas.clear()
        medias.clear()
        lista.append(alunos[:])
        alunos.clear()
        o = ' '
        while o not in 'SN':
            o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if o == 'N':
            break
    print('~'*23)
    print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
    print('~' * 23)
    for i, n in enumerate(lista):
        print(f'{i:<4}{lista[i][0]:<10}{lista[i][2][0]:>8.1f}')
    resp = int(input('Deseja mostrar as notas de qual aluno? '))
    while resp != 999:
        print(f'As notas de {lista[resp][0]} são {lista[resp][1]}.')
        resp = int(input('Deseja mostrar as notas de qual aluno? '))
        if resp == 999:
            break
    break

# Primeira parte do código pode ser assim, mais enxuto:
lista = []
while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    n1 = float(input('Digite a 1a nota: '))
    n2 = float(input('Digite a 1a nota: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])