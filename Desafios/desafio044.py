p = float(input('Digite o preço do produto: R$ '))
print('Qual o método de pagamento?'
      '\n1 para dinheiro/pix'
      '\n2 para 1x no cartão'
      '\n3 para 2x no cartão'
      '\n4 para 3x ou mais no cartão com juros de 20%')
m = int(input('Insira: '))
if m == 1:
      print(f'Em dinheiro/pix, o produto custa R$ {p*0.9:.2f}.')
elif m == 2:
      print(f'Em 1x no cartão, o produto custa R$ {p*0.95:.2f}.')
elif m == 3:
      print(f'Em 2x no cartão, o produto custa R$ {p:.2f} e cada parcela será de R$ {p / 2:.2f}.')
elif m ==4:
      par = int(input('Quantas parcelas? '))
      print(f'Em 3x ou mais no cartão, o produto custa R$ {p*1.2:.2f}. '
            f'Sua compra será parcelada em {par}x de R$ {(p*1.2) / par:.2f}.')
else:
      print('OPÇÃO INVÁLIDA. DIGITE UM NÚMERO ENTRE 1 E 4')
