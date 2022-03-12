from time import sleep
print('\33[1;32;107m~\33[m'*25)
print('\33[1;32;107mEMPRÉSTIMO PESSOAL ONLINE\33[m')
print('\33[1;32;107m~\33[m'*25)
print('\n\33[1;30;107mAGUARDE UM MOMENTO\33[m')
sleep(2)
nome = str(input('\n\33[36mPor favor, digite seu nome completo:\33[m ')).strip().title()
renda = float(input('\n\33[36mQual sua renda atual?\33[m '))
emprestimo = int(input('\n\33[36mQual o valor desejado para empréstimo?\33[m '))
anos = int(input('\n\33[36mEm quantos anos deseja finalizar seu empréstimo?\33[m '))
'\n'
print('\n\33[1;35;107mNossos especialistas estão avaliando a viabilidade do seu empréstimo,\33[m'
      '\n\33[1;35;107mPor favor, aguarde uns instantes.\33[m')
sleep(5)
meses = anos*12
parcela = emprestimo / meses
if parcela <= (renda*0.3):
    print(f'\n\33[1;32;107mParabéns, {nome}! Seu empréstimo foi \33[m\33[4;32;107mAPROVADO\33[1;32;107m.\33[m '
          f'\n\33[1;32;107mO valor de cada parcela será R$ \33[m\33[4;33;107m{parcela:.2f}\33[m')
else:
    print(f'\n\33[7;31;40mSinto muito, {nome}. Infelizmente seu empréstimo foi \33[4;30;43mNEGADO\33[m '
          f'\n\33[7;31;40mA prestação seria R$ \33[4;33;107m{parcela:.2f}\33[m\33[7;31;40m Mas você pode tentar novamente \33[m'
          f'\33[7;31;40mpara um período maior de tempo.\33[m')
