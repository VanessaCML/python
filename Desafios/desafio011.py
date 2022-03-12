print('TINTE.ME - Quantos litros de tinta vou usar?')
c = float(input('Qual o comprimento da sua parede em metros? '))
a = float(input('Qual a altura da sua parede em metros? '))
print(f'Sua parede tem {a*c:.2f}m², logo você precisará de {(a*c)/2:.2f}L de tinta.')
