nome = str(input('Digite seu nome: ')).title()
if nome == 'Vanessa':
    print(f'Que nome legal, {nome}!')
elif nome == 'Ana' or nome == 'Neide' or nome == 'Liu':
    print(f'Seu nome é muito bonito, {nome}!')
elif nome in 'Julia Maria Larissa':
    print(f'Seu nome é muito popular no Brasil, {nome}!')
else:
    print(f'Seu nome é bem meh, {nome}...')
print(f'Tenha um bom dia!')
