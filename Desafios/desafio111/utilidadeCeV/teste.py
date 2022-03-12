from desafio111.utilidadeCeV import moeda, dado

# num = float(input('Digite um valor: R$ '))  # Desafio 111
num = dado.leiaDinheiro('Digite um número: ')
moeda.resumo(num, 10, 25)
