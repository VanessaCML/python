soma = 0
maior = 0
menor = 0
nomevelho = ''
for pes in range(1, 5):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (F/M): ')).strip().upper()
    soma += idade
    if sexo in 'Mm':
        if pes == 1:
            maior = idade
            nomevelho = nome
        else:
            if idade > maior:
                maior = idade
                nomevelho = nome
    if sexo in 'Ff':
        if idade < 20:
            menor += 1
print(f'A média de idade do grupo é de {soma/4}')
if maior == 0:
    print(f'Não há homens nesse grupo.')
else:
    print(f'O homem mais velho tem {maior} anos e se chama {nomevelho}.')
if menor == 1:
    print(f'Há apenas {menor} mulher com menos de 20 anos.')
if menor == 0:
    print(f'Não há nenhuma mulher com menos de 20 anos.')
if menor > 1:
    print(f'Há {menor} mulheres com menos de 20 anos.')




'''    if pes == 1 and sexo in 'Mm':
        maior = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomemaisvelho = nome'''