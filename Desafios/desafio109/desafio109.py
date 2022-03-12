import moeda
num = float(input('Digite um valor: R$ '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}.'
      f'\nA metade de {moeda.moeda(num)} é {moeda.metade(num, True)}.'
      f'\nO valor {moeda.moeda(num)} acrescido de 10% é {moeda.aumentar(num, 10, True)}.'
      f'\nO valor {moeda.moeda(num)} descontado em 10% é {moeda.diminuir(num, 10, True)}.')
