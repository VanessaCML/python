soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont += 1
        soma += n
if cont != 1 and cont != 0:
    print(f'A soma dos {cont} números é igual a {soma}.')
elif cont == 1:
    print(f'Só há {cont} número par que é o {soma}.')
elif cont == 0:
    print('Não há nenhum número par.')
