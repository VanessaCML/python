import moeda
num = float(input('Digite um valor: R$ '))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.'
      f'\nA metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.'
      f'\nO valor {moeda.moeda(num)} acrescido de 10% é {moeda.moeda(moeda.aumentar(num, 10))}.'
      f'\nO valor {moeda.moeda(num)} descontado em 10% é {moeda.moeda(moeda.diminuir(num, 10))}.')
