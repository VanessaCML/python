'''tempo = int(input('Quantos anos tem seu carro? '))
f = 'FIM'
if tempo<=3:
    print('Carro novo!')
else:
    print('Tá na hora de trocar!')
print(f'{f:=^10}')'''


'''OU'''

'''tempo = int(input('Quantos anos tem seu carro? '))
f = 'FIM'
print('Carro novinho, hein!'if tempo<=3 else 'Tá na hora de trocar essa lata velha!')
print(f'{f:=^10}')'''


'''nome = str(input('Qual seu nome? '))
if nome == 'Vanessa':
    print('Que nome bonito!')
else:
    print('Que nome sem graça, hein!')
f = 'FIM'
print(f'{f:*^15}')'''

import emoji
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A média é {m:.1f}.')
print(emoji.emojize('Aluno aprovado! :ok_hand:', use_aliases=True) if m>=6 else (emoji.emojize('Aluno reprovado :boom:',
                                                                                               use_aliases=True)))









