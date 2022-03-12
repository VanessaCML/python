import emoji
v = int(input('\33[1;32mQual a velocidade do carro?\33[m '))
if v > 80:
    print(emoji.emojize(f'\n\33[1;31mMULTADO! Você excedeu o limite de velocidade permitido :police_car: '
                        f'\nSerá aplicada uma multa no 'f'valor de R$ \33[33;107m{(v - 80) * 7} :moneybag:\33[m',
                        use_aliases=True))
else:
    print('\n\33[32;107mVocê está dentro da velocidade máxima permitida que é 80Km/h.\33[m ')
print(emoji.emojize('\n\33[97;40mTenha uma boa viagem! :car:\33[m \n\33[97;40m**Use o cinto de segurança**\33[m',
                    use_aliases=True))
