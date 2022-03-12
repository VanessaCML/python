print('-'*8)
print('SETOR RH')
print('-'*8)
print('AGUARDE UM MOMENTO, POR FAVOR...')
from time import sleep
sleep(2)
nome = str(input('\nSeja bem-vindo(a)! Por favor, digite seu nome: ')).strip().title()
s = float(input('\nInsira seu salário atual, por favor: '))
a = s*1.15 if s<=1250 else s*1.1
print('\nCalculando seu novo salário.'
      '\nPor favor, aguarde...')
sleep(3)
print(f'\nParabéns, {nome}! Você ganhou um aumento e seu novo salário a partir de Fevereiro deste ano será R$ {a:.2f}.')
