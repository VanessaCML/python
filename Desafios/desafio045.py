print('\33[1;35m*\33[m' * 20)
l = ' JOKENPO '
print(f'\33[1;35m{l:=^20}\33[m')
print('\33[1;35m*\33[m' * 20)
from random import randint
c = randint(0, 2)
itens = ('pedra', 'papel', 'tesoura')
print('\n\33[33mEscolha entre as opções:\33[m'
      '\n\33[33m0 - PEDRA\33[m'
      '\n\33[33m1 - PAPEL\33[m'
      '\n\33[33m2 - TESOURA\33[m')
j = int(input('\33[1;97mDigite:\33[m '))
if j > 2:
    print('\33[1;35m-=-\33[m' * 20)
    print(f'\33[1;31m          OPÇÃO INVÁLIDA       TENTE NOVAMENTE\33[m')
    print('\33[1;35m-=-\33[m' * 20)
else:
    from time import sleep
    print('\n\33[1;32mJO\33[m')
    sleep(1)
    print('\33[1;33mKEN\33[m')
    sleep(1)
    print('\33[1;34mPO\n\33[m')
    print('\33[1;35m-=-\33[m'*20)
    if c == j:
        print(f'\33[1;35mEMPATE! Você jogou {itens[j]} e o computador jogou {itens[c]}.\33[m')
    elif j == c + 1 or j == c - 2:
        print(f'\33[1;35mVocê ganhou! Você jogou {itens[j]} e o computador jogou {itens[c]}.\33[m')
    elif j == c + 2 or j == c - 1:
        print(f'\33[1;35mVocê perdeu! Você jogou {itens[j]} e o computador jogou {itens[c]}.\33[m')
    print('\33[1;35m-=-\33[m'*20)

