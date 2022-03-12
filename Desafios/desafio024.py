cidade = input('Qual o nome da sua cidade? ')
c = cidade.lstrip()
a = c.capitalize()
resposta = a.find('Santo'[:5])
print('Sua cidade começa com "Santo"? ', resposta==0)

#cidade = input('Em que cidade você nasceu? ').title().split()
#print(cidade[0] == 'Santo')

#cidade = str(input('Digite uma cidade: ')).upper().strip().split()
#print('Essa cidade começa com SANTO? {}'.format('SANTO' in cidade[0]))
