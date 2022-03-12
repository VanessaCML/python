infojogs = []
while True:
    jogador = {}
    gols = []
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, n):
        gols.append(int(input(f'     Quantos gols {jogador["nome"]} marcou na partida {c+1}: ')))
        jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    infojogs.append(jogador.copy())
    while True:
        o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if o not in 'SN':
            print('Desculpe, não entendi...')
        break
    if o == 'N':
        break
print('~'*42)
print(f'{"CÓD":<6}{"NOME":<10}{"GOLS":^15}{"TOTAL":>10}')
print('~'*42)
for i, v in enumerate(infojogs):
    print(f'{i+1:<6}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('~'*42)
while True:
    r = int(input('Deseja mostrar os dados de qual jogador? [999 interrompe o programa] '))
    print('~' * 70)
    if r == 999:
        break
    if r > len(infojogs) or r == 0:
        print(f'Erro! Não existe jogador com código {r}.')
    else:
        print(f'Levantamento do jogador {infojogs[r-1]["nome"]}')
        for i, gol in enumerate(infojogs[r-1]['gols']):
            print(f'Na partida {i+1} ele fez {gol} gol(s).')
    print('~'*70)
print('<<<VOLTE SEMPRE>>>')
