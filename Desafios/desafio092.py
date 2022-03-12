from datetime import datetime
lista = {}
lista['nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
lista['idade'] = datetime.now().year - ano
lista['CTPS'] = int(input('Carteira de trabalho (digite 0 caso não tenha): '))
if lista['CTPS'] != 0:
    lista['contratação'] = int(input('Ano de contratação: '))
    lista['salário'] = float(input('Salário: '))
    lista['aposentadoria'] = (35 - (datetime.now().year - lista['contratação'])) + lista['idade']
print(lista)
for k, v in lista.items():
    print(f'{k.title()} tem o valor {v}.')
