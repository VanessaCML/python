import moeda
num = float(input('Digite um valor: R$ '))
t = 'R$'
print(f'O dobro de {num} é {moeda.dobro(num):.2f}.'
      f'\nA metade de {num} é {moeda.metade(num):.2f}.'
      f'\nO valor {num} acrescido de 10% é {moeda.aumentar(num, 10):.2f}.'
      f'\nO valor {num} descontado em 10% é {moeda.diminuir(num, 10):.2f}.')
