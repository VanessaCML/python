d = float(input('Qual a distância a ser percorrida em Km? '))
p = d * 0.5 if d <= 200 else d * 0.45
print(f'O valor da passagem é R$ {p:.2f}.')



'''if d<=200:
    print(f'O valor da passagem é R$ {d*0.5:.2f}.')
else:
    print(f'O valor da passagem é R$ {d*0.45:.2f}.')'''