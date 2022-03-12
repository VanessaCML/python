alunos = {'nome': str(input('Nome: ')).strip().title()}
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 6:
    alunos['situação'] = 'APROVADO'
else:
    alunos['situação'] = 'REPROVADO'
for k, v in alunos.items():
    print(f'{k.title()} é {v}.')
